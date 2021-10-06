from django.urls import path
from django.views.generic import TemplateView

from producerapp.views import PlayCreateView

app_name = 'producerapp'

urlpatterns = [
    path('play/',PlayCreateView.as_view(),name='play'),
]