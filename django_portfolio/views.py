from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.views import View
from django.template.loader import render_to_string

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import *

from pprint import pprint
class BaseView(TemplateView):
	title = 'Default Title'
	template_name = 'layout/base.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = self.title
		return context

class HomeView(BaseView):
	template_name = 'django_portfolio/index.html'
	title = 'Home'

class RegisterView(BaseView):
	title = 'register'

class TestView(BaseView):
	template_name = 'django_portfolio/test_page.html'
	title = 'Test'