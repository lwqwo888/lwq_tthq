from django.shortcuts import render
from django.http import HttpResponse

def register(request):
    return render(request,'User/register.html')
def login(request):
    return render(request,'User/login.html')