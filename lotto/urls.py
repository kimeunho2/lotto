from django.contrib import admin
from django.urls import path
from lotto import views


urlpatterns = [
    path('', views.LottoView.as_view(), name="lotto")
]