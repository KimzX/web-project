
from . import views
from django.urls import path

urlpatterns = [
    path("index",views.index),
    path("login",views.login),
    path("page1",views.pageone),
    path("page2",views.pagetwo),
    path("page3",views.pagethree),
    path("page4",views.pagefour),
    path("regester",views.reg)
]  




