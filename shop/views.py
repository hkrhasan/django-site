from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,'shop/index.html')

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse('we are at contact')

def tracker(request):
    return HttpResponse('we are at tracking view')

def search(request):
    return HttpResponse('we are at search')

def productView(request):
    return HttpResponse('we are at product view')

def checkout(request):
    return HttpResponse('we are at checkout')