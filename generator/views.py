from django.shortcuts import render
from django.http import HttpResponse
import random
def home(request):
    return render(request, 'generator/home.html')
# Create your views here.
def password(request):
    length = int(request.GET.get('length', 12))
    chars = list('qwertyuiopasdfghjklzxcvbnm')
    if request.GET.get('uppercase'):
        chars += list('QWERTYUIOPLKJHGFDSAMNBVCXZ')
    if request.GET.get('numbers'):
        chars += list('1234567890')
    if request.GET.get('special'):
        chars += list('!@#$%&*)+_=')
    
    
    
    thepass = ''
    for i in range (length):
        thepass += random.choice(chars)
    return render(request, 'generator/password.html', {'password':thepass})
def about(request):
    return render(request, 'generator/about.html')