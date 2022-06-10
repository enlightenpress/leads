from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def index(request): 
    return HttpResponse("Hello World!")

def home(request):
    response = redirect('/admin')
    return response
