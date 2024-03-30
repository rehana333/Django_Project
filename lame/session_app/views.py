from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def set_session(request):
    request.session['username'] = 'Tattu'
    return HttpResponse("Session Set")
def get_session(request):
    username = request.session.get('username', 'Guest')
    return HttpResponse("User: "+ username)
