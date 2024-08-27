from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<em>Hello World! This is my first app</em>")

# Create your views here.
def printuuid(request):
    import uuid
    return HttpResponse(str(uuid.uuid4()))
