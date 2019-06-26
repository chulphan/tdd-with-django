import sys
from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages
from accounts.models import Token
from django.contrib import auth
from accounts.authentication import PasswordlessAuthenticationBackend

def send_login_email(request):
    email = request.POST['email']
    token = Token.objects.create(email=email)
    url = request.build_absolute_uri(
        reverse('login') + '?token=' + str(token.uid)
    )
    message_body = f'Use this link to login:\n\n{url}'
    send_mail(
        'Your login link for TddTutorial',
        message_body,
        'noreply@tddtutorial',
        [email]
    )
    messages.success(
        request,
        "Check your email, we've sent you a link you can use to login"
    )
    return redirect('/')

def login(request):
    user = PasswordlessAuthenticationBackend().authenticate(uid=request.GET.get('token'))
    if user:
        auth.login(request, user)
    return redirect('/')

def logout(request):
    print(request)
    auth.logout(request)
    return redirect('/')
