from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return render(request, "index.html")


def get_name(request, name):
    return render(request, "persons.html", {'name': name})
