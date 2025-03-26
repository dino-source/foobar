from django.shortcuts import HttpResponse


def index():
    return HttpResponse("Hello, world. You're at the polls index.".encode("utf-8"))
