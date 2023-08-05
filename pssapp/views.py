from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"pssapp/index.html")
def about(request):
    return HttpResponse("This is about us page")
def ourprocesses(request):
    return HttpResponse("This is Our processes page")
def valuedpartners(request):
    return HttpResponse("This is valuedpartners")
def contact(request):
    return HttpResponse("This is contact us page")
def careers(request):
    return HttpResponse("This is Careers page")
def emplogin(request):
    return HttpResponse("This is employee login page")
