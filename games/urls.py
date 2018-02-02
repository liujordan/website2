from django.urls import path, re_path, include
from .views import *
urlpatterns = [
    path('clicker', ClickerView.as_view(), name='clicker'),
]