from django.urls import path

from . import views

urlpatterns = [
    path("",views.fun1),
    path("fun2/",views.fun2),
    path("fun3/",views.fun3),
    path("fun1/",views.fun1),
]
