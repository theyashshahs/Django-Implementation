from django.http import HttpResponse

def hello(req):
    return HttpResponse("<h1> BRILLIANT MINDS AT WORK</h1>")