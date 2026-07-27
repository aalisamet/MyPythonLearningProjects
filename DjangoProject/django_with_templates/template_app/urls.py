from django.urls import path
from . import views

urlpatterns =[
    path("firstview/", views.first_temp,name="template")


]