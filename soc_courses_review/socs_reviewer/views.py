from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'To be replaced with HTML'}
    return render(request, 'socs_reviewer/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': 'To be replaced with HTML'}
    return render(request, 'socs_reviewer/about.html', context=context_dict)

# Create your views here.
