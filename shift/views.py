from django.shortcuts import render


def index(request):
    return render(request, "shift/home.html")


def about(request):
    return render(request, "shift/about.html")
