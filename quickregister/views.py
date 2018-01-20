from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.template.loader import render_to_string

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import *

class LoginView(TemplateView):
	title = 'Login Page'
	template_name = 'quickregister/index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = self.title
		return context

	def post(self, request, *args, **kwargs):
		form = UserLoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(request, username=username, password=password)
			if user:
				login(request, user)
			else:
				print("ATTEMPTED TO LOGIN WITH WRONG USER CREDENTIALS")
				print(username)
				print(password)

class UserCreate(CreateView):
	model = User
	fields = ['username', 'password', 'email']