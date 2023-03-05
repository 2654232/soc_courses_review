from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the SOCS Reviewer <a href='/socs_reviewer/about/'>About</a>.")

def about(request):
    return HttpResponse("This is the about page (to be changed later) <a href='/socs_reviewer/'>Index</a>.")

# Create your views here.
