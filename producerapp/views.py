from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from producerapp.forms import PlayCreationForm
from producerapp.models import Play


class PlayCreateView(CreateView):
    model = Play
    form_class = PlayCreationForm
    context_object_name = 'target_play'
    template_name = 'producerapp/producer.html'

    def get_success_url(self):
        return reverse('mainpageapp:mainpage')