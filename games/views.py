from django.shortcuts import render
from django_portfolio.views import BaseView

class ClickerView(BaseView):
	title = 'Clicker Game'
	template_name = 'games/clicker.html'

class PondsView(BaseView):
    title = 'Ponds'
    template_name = 'games/ponds.html'
    
class ShapesView(BaseView):
    title = 'Shapes'
    template_name = 'games/shapes.html'
