from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def set_cookie(request):
    response = HttpResponse("Cookie Set")
    response.set_cookie('username', 'Tattu')
    return response
def get_cookie(request):
    username = request.COOKIES.get('username', 'Guest')
    return HttpResponse("User: "+ username)
