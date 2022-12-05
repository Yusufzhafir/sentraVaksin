from django.shortcuts import render

from dummy.views import index

# Create your views here.

def index(request):
    return render(request,'Home.html')

