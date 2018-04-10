from django.urls import path, re_path, include
from .views import *
urlpatterns = [
    path('clicker', ClickerView.as_view(), name='clicker'),
    path('ponds', PondsView.as_view(), name='ponds'),
    path('shapes', ShapesView.as_view(), name='shapes'),
]