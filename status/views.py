from django.shortcuts import render
from django.http import HttpResponse

#def index(request):
 #   return HttpResponse("Hello, world!")

def index(request):
    context = {}
    return render(request, "status/board.html", context)