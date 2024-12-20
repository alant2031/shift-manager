from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello HOME!")


def about(request):
    return HttpResponse("Hello ABOUT!")
