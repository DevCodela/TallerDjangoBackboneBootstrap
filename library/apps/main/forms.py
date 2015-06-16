from django import forms 
from django.contrib.auth.models import User

class LoginForm(forms.Form):

	username = forms.CharField(max_length=50,
				widget = forms.TextInput(attrs = {
						"type" : "text",
						"placeholder" : "Username",
						"class" : "my_class"
					}))
	password = forms.CharField(max_length=50,
				widget = forms.TextInput(attrs = {
						"type" : "password",
						"placeholder" : "Password",
						"class" : "my_class"
					}))

	def clean(self):
		username_exist = User.objects.filter(
				username = self.cleaned_data['username']
			).exists()
		if not username_exist:
			self.add_error("username", "El username no existe")
		else:
			user = User.objects.get(
					username = self.cleaned_data['username']
				)
			if not user.check_password(self.cleaned_data['password']):
				self.add_error("password", "El password no coincide")