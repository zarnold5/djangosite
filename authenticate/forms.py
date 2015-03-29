from django import forms 
from brother.models import Brother 
from django.forms import ModelForm

class LoginForm(ModelForm):
	email = forms.CharField(label=(u'Email Address'))
	password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
	class Meta:
		model = Brother
		exclude = ('user', 'position')