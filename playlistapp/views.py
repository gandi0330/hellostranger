from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
import csv
import pandas as pd

from playlistapp.models import Play


# csv 파일을 읽어 모델에 넣는 함수입니다
# 일회성 기능으로 직접 url을 입력하면 실행됩니다
# 기존 연극 정보를 모두 지우고 csv파일의 내용으로 업데이트 합니다
# 예시 : http://127.0.0.1:8000/playlist/csv_read/
def readcsv(request):
    Play.objects.all().delete()

    #data_df_1.csv 파일은 현재 views.py 폴더와 같은 위치에 있습니다
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