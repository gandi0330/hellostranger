import numpy as np
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin, ListView

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from profileapp.models import Profile

import pandas as pd
import numpy as np
from random import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_squared_error
import warnings; warnings.filterwarnings('ignore')
has_ownership = [account_ownership_required, login_required]




class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('mainpageapp:mainpage')
    template_name = 'accountapp/create.html'



class AccountDetailView(DetailView):
    model = User
    context_object_name =  'target_user'
    template_name = 'accountapp/detail.html'

    # paginate_by = 25

    # def get_context_data(self, **kwargs):
    #     object_list = Article.objects.filter(writer=self.get_object())
    #     return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('mainpageapp:mainpage')
    template_name = 'accountapp/update.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'


def doSomething(request, pk):
    post = get_object_or_404(Profile,pk=pk)
    consumer_list = [[post.play1_title, post.play1_rate],[post.play2_title,post.play2_rate],[post.play3_title,post.play3_rate]]

    recommend_list = ai(consumer_list)
    # recommend_list = [['test1','3'],['test2','4.2'],['test3','3.2']]
    context = {'object' : recommend_list}
    return render(request, 'accountapp/consumer.html', context)

def ai(consumer_list):
    plays = pd.read_excel('C:/Users/comn/PycharmProjects/recommendproject/accountapp/play_data.xlsx')
    ratings = pd.DataFrame({'userid':[1 for i in range(len(consumer_list))],
                            'playid':[ plays.index[plays['title'] == x[0]].tolist()[0] for x in consumer_list],
                            'rating':[float(x[1]) for x in consumer_list]})
    vote_avg = []
    vote_cnt = []
    for i in range(len(plays)):
        rating = np.round(uniform(1,5), 1)
        vote_avg.append(rating)
        cnt = randint(0, 500)
        vote_cnt.append(cnt)
    plays['vote_average'] = vote_avg
    plays['vote_count'] = vote_cnt
    def weighted_vote_average(record):
        C = plays['vote_average'].mean()
        m = plays['vote_count'].quantile(0.6)
        v = record['vote_count']
        R = record['vote_average']
        return ( (v/(v+m)) * R) + ( (m/(v+m)) * C )
    plays['weighted_vote'] = plays.apply(weighted_vote_average, axis=1)
    def find_sim_play(plays, sorted_ind, title_name, top_n=10):
        title_play = plays[ plays['title'] == title_name]
        title_index = title_play.index.values
        sim_indexs = sorted_ind[ title_index, :top_n*3 ]
        sim_indexs = sim_indexs.reshape(-1)
        sim_indexs = sim_indexs[ sim_indexs != title_index ]
        return plays.iloc[sim_indexs].sort_values('weighted_vote', ascending=False)[:top_n]
    ratings.pivot_table(values='rating', index='userid', columns='playid')
    rating_plays = pd.merge(ratings, plays, on='playid')
    ratings_mat = rating_plays.pivot_table(values='rating', index='userid', columns='title')
    ratings_mat = ratings_mat.fillna(0)
    ratings_mat_T = ratings_mat.T
    item_sim = cosine_similarity(ratings_mat_T, ratings_mat_T)
    item_sim_df = pd.DataFrame(item_sim, index=ratings_mat.columns, columns=ratings_mat.columns)
    def get_unseen_plays(ratings_matrix, userid):
        user_id = ratings_matrix.loc[userid, :]
        return user_id[ user_id <= 0 ].index.values.tolist()
    unseen_list = get_unseen_plays(ratings_mat, 1)
    def predict_rating_topsim(ratings_arr, item_sim_arr, n=20):
        pred = np.zeros(ratings_arr.shape)
        for col in range(ratings_arr.shape[1]):
            top_n_items = item_sim_arr[:, col].argsort()[:-n-1:-1]
            for row in range(ratings_arr.shape[0]):
                S = item_sim_arr[col, :][top_n_items]
                R = ratings_arr[row, :][top_n_items]
                pred[row, col] = R.dot(S) / np.sum(np.abs(S))
        return pred
    ratings_pred2 = predict_rating_topsim(ratings_mat.values, item_sim_df.values, 20)
    ratings_pred2_mat = pd.DataFrame(ratings_pred2,
                                    index=ratings_mat.index,
                                    columns=ratings_mat.columns)
    def recomm_play_by_userid(pred_df, userid, unseen_list, top_n=10):
        result_list = []
        result = pred_df.T[userid].sort_values(ascending=False)[:top_n]
        for i in range(len(result)):
            result_list.append([result.index[i],result.values[i]])
        return result_list

    return recomm_play_by_userid(ratings_pred2_mat, 1, unseen_list, 5)