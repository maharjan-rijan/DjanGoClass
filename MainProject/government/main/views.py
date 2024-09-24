from django.shortcuts import render
from .models import *
def homePage(request):
    return render(request, 'home.html')

def homeDetail(request, id):
    homeDetail = Home.objects.get(id=id)
    return render(request, 'homeDetail.html')