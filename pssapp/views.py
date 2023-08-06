from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"pssapp/index.html")
def about(request):
    return render(request,"pssapp/about.html")
def ourprocesses(request):
    return render(request,"pssapp/ourprocesses.html")
def valuedpartners(request):
    return render(request,"pssapp/valuedpartners.html")
def contact(request):
    return render(request,"pssapp/contact.html")
def careers(request):
    return render(request,"pssapp/careers.html")

