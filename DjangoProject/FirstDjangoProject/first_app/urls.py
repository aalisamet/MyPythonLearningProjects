from django.urls import path
from . import views

from django.urls import path


urlpatterns = [
    path("first_app", views.about_view,name = "about_view"),
]
