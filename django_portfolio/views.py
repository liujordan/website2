from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.views import View
from django.template.loader import render_to_string

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import *

from pprint import pprint
from .projects import *
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


class ProjectsView(BaseView):
	title = 'Projects'
	template_name = 'django_portfolio/projects.html'
	scroll_bar_length = 100.
	scroll_bar_line_num = 50
	projects = [
		Item('project-python', 'python', icon='devicon-python-plain', scale=1, scroll_bar_length=scroll_bar_length,
			description='I\'ve been using python from first year until now and I am in love with it.' +\
			'This site, for example, was built using the Django framework which is written in python.')
	]
	def get_scroll_bar_line_html(self):
		out = ''
		width = self.scroll_bar_length/self.scroll_bar_line_num
		for i in range(self.scroll_bar_line_num):
			elm_class = 'line'
			if i % 10 == 0:
				elm_class += ' bline'
			elif i % 5 == 0:
				elm_class += ' mline'

			msg = ''
			if i == 0:
				msg = '<span>Learning</span>'
			elif i == self.scroll_bar_line_num // 2:
				msg = '<span>Capable</span>'
			elif i == self.scroll_bar_line_num - 1:
				msg = '<span>Proficient</span>'


			out += '<div class="%s">%s</div>' % (elm_class, msg)
		return out


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['projects'] = [project.scroll_bar_html() for project in self.projects]
		context['lines'] = self.get_scroll_bar_line_html()
		context['js'] = ['<script type="text/javascript">'] + \
		[ project.item_content_js() for project in self.projects] + \
						['</script>']
		return context