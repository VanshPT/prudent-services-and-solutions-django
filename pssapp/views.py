from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(response):
    return HttpResponse("This is Home Page")
def about(response):
    return HttpResponse("This is about us page")
def training(response):
    return HttpResponse("This is training and Recruitment page")
def ourstrength(response):
    return HttpResponse("This is our strength page")
def welfare(response):
    return HttpResponse("this is welfare page")
def contact(response):
    return HttpResponse("This is contact us page")
def emplogin(response):
    return HttpResponse("This is employee login page")
