from django.urls import path

from selectpage.views import selectpage

app_name = 'selectpage'

urlpatterns = [
    path('selectpage/',selectpage, name='selectpage')
]