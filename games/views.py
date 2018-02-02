from django.shortcuts import render
from django_portfolio.views import BaseView

class ClickerView(BaseView):
	title = 'Clicker Game'
	template_name = 'games/clicker.html'
