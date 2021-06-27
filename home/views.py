from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>This is Home page. </h1>")

def about(request):
    return HttpResponse("<h1>This is About Page. </h1>")

def services(request):
    return HttpResponse("<h1>This is Services page. </h1>")

def contacts(request):
    return HttpResponse("<h1>This is Contacts page. </h1>")