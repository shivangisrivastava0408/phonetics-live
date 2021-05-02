from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate
from account.models import Account

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(max_length=60, help_text='Enter your email')
	age = forms.IntegerField(help_text='Enter age')
	name = forms.CharField(max_length=60, help_text='Enter name')
	username = forms.CharField(max_length=20, help_text='Enter username')

	class Meta(UserCreationForm.Meta):
		model = Account
		fields = ('email', 'name', 'username', 'age', 'password1', 'password2')

	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.name = self.cleaned_data['name']
		user.email = self.cleaned_data['email']
		user.username = self.cleaned_data['username']
		user.age = self.cleaned_data['age']

		if commit:
			user.save()
		return user

class AccountAuthenticationForm(forms.ModelForm):
	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('email', 'password')

	def clean(self):
		email = self.cleaned_data['email']
		password = self.cleaned_data['password']
		if not authenticate(email=email, password=password):
			raise forms.ValidationError("Invalid login")



class MyUserChangeForm(UserChangeForm):
	class Meta(UserChangeForm.Meta):
		model = Account