from django.shortcuts import render, redirect
from django.core.mail import send_mail

def home(request):
	return render(request, "main.html")

def submit(request):
	email = request.GET['email']
	print email
	send_mail('StaticGap - ' + email, "EMAIL: " + email, 'nort.ryan@gmail.com', ['nort.ryan@gmail.com'],fail_silently=False)

	return redirect('/')
