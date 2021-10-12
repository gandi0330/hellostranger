from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView, \
    ArticleListView, recommend, test

app_name = 'accountapp'

urlpatterns =  [
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
    path('mainpage/<int:pk>',ArticleListView.as_view(), name='mainpage'),
    path('recommend/<int:pk>', recommend, name='recommend'),
    path('area/<int:pk>', test,name='area'),

]