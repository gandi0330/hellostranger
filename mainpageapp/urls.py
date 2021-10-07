from django.urls import path

from mainpageapp.views import mainpage, ArticleListView

app_name = 'mainpageapp'

urlpatterns = [
    path('mainpage/',ArticleListView.as_view(), name='mainpage')

]