from django.shortcuts import render, redirect
from account.models import Account
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm
import speech_recognition as sr
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.http import JsonResponse

def welcome(request):
	if request.user.is_authenticated:
		return render(request, 'index.html', {})
	return render(request, 'register.html', {})

'''def speech(request):
	r = sr.Recognizer()
	#print(request.FILES['audio'])
	#f = request.FILES.get('data')
	#audio_file=sr.AudioFile(f)
	#abc=static('Audio/harvard.wav')
	audio_file = sr.AudioFile('templates/testing.wav')
	with audio_file as source: 
	   r.adjust_for_ambient_noise(source) 
	   audio = r.record(source)
	result = r.recognize_google(audio)
	return render(request, 'speech_page.html', {'a':result})'''

def play(request):
	return render(request, 'recording.html',{})

def register(request):
	if request.user.is_authenticated:
		return redirect('welcome')
	context = {}
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			return redirect('welcome')
		else:
			print(form.errors)
			context['registration_form'] = form
	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'register.html', context)

def logout_view(request):
	logout(request)
	return redirect('register')

def login_view(request):
	context = {}
	user = request.user
	if user.is_authenticated:
		return redirect('welcome')

	if request.method == 'POST':
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)
			if user:
				login(request, user)
				return redirect('welcome')
	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form
	return render(request, 'login.html', context)