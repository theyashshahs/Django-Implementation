from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.



def fun1(req):
    return render(req,"test1.html")

def fun2(req):
    return render(req,"test2.html")

def fun3(req):
    return render(req,"test3.html")

    