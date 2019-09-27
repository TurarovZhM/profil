from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def about(request):
    return render(request, 'profileapp/about.html', {'title': 'About', 'textforthispage': 'About me'})


def publications(request):
    return render(request, 'profileapp/publications.html', {'title': 'Publications', 'textforthispage': 'My Publications'})

def contact(request):
    return render(request, 'profileapp/contact.html', {'title': 'Contact me', 'textforthispage': 'Contact with me'})

