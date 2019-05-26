from django.contrib import admin
from django.urls import path ,include
from resume import urls ,views

urlpatterns = [
    path('', views.index),

]
