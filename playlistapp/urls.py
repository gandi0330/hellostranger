from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView, \
    ArticleListView, recommend
from playlistapp.views import readcsv

app_name = 'playlistapp'

urlpatterns =  [

    path('csv_read/', readcsv, name='readcsv'),
]