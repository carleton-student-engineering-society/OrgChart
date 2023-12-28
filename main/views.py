# from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the index.")


def search(request):
    pass


def search_pattern(request, pattern: str):
    pass


def view(request):
    pass


def view_org(request, org: str):
    pass


def add(request, org: str):
    pass


def create_org(request):
    pass
