from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin, ListView

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from profileapp.models import Profile

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

