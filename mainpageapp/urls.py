from django.urls import path

from mainpageapp.views import mainpage

app_name = 'mainpageapp'

urlpatterns = [
    path('mainpage/',mainpage, name='mainpage')
]