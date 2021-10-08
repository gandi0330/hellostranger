import pandas as pd
import numpy as np
from random import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_squared_error
import warnings; warnings.filterwarnings('ignore')
def ai(consumer_list):
    plays = pd.read_excel('/play_data.xlsx')
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