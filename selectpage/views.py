from django.shortcuts import render

# Create your views here.
def selectpage(request):
    return render(request,'selectpage/selectpage.html')
