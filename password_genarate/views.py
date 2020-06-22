from django.shortcuts import render
import random

def home(request):
    return render(request, 'password_genarate/base.html', {'password':'aefeefqdqad'})

def new_password(request):
    charecter = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        charecter.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')) 
    if request.GET.get('lowercase'):
        charecter 
    if request.GET.get('numaric'):
        charecter.extend(list('1234567890')) 
    if request.GET.get('spical'):
        charecter.extend(list('~!@#$%^&*')) 

    
    length = int(request.GET.get('length'))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(charecter)

    return render(request,'password_genarate/password.html', {'password':thepassword})

def new_about(request):
    
    return render(request, 'password_genarate/about.html', {'aboutdata':'new data for app'})