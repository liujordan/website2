from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template.loader import render_to_string

class BaseView(TemplateView):
	title = 'Default Title'
	template_name = 'layout/base.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = self.title
		return context

class HomeView(BaseView):
	template_name = 'home/index.html'
	title = 'Home'
class TestView(BaseView):
	template_name = 'home/test_page.html'
	title = 'Test'