from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login

from .forms import LoginForm

class HomeView(FormView):

	template_name = 'home.html'
	form_class = LoginForm
	success_url = reverse_lazy("home")

	def form_valid(self, form):
		user = authenticate(
				username = form.cleaned_data['username'],
				password = form.cleaned_data['password']
			)
		if user is not None:
			login(self.request, user)
			return super(HomeView, self).form_valid(form)

class DetalleView(TemplateView):

	template_name = "detalle.html"
