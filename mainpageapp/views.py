from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from producerapp.models import Play


def mainpage(request):
    return render(request,'mainpageapp/mainpage.html')



class ArticleListView(ListView):
    model = Play
    context_object_name = 'play_list'
    template_name = 'mainpageapp/mainpage.html'
