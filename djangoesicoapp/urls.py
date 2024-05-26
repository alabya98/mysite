from django.urls import path
from . import views

urlpatterns = [
    path('gender', views.index_gender),
]
