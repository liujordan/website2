from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template.loader import render_to_string
class HomeView(TemplateView):
	template_name = 'home/index.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['wowzers'] =  'i made a custom context lol'
		return context
