from django.shortcuts import render

# Create your views here.

def mainpage(request):
    return render(request,'mainpageapp/mainpage.html')