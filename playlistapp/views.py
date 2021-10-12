from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
import csv
import pandas as pd

from playlistapp.models import Play


def readcsv(request):
    Play.objects.all().delete()

    url = 'C:/Users/comn/PycharmProjects/recommendproject/playlistapp/data_df_1.csv'


    with open(url,'r') as f:
        dr = csv.DictReader(f)
        s = pd.DataFrame(dr)
    ss = []

    for i in range(len(s)):
        st = (s['title'][i], s['genres'][i],s['area'][i],
              s['vote_average'][i],s['vote_count'][i])
        ss.append(st)

    for i in range(len(s)):
        Play.objects.create(title=ss[i][0], genres=ss[i][1], area = ss[i][2],rate=ss[i][3],vote=ss[i][4])


    return HttpResponse("<div>완료!!</div>")