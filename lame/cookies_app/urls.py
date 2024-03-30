from django.urls import path
from cookies_app import views

urlpatterns = [
    
    path('set-cookie/', views.set_cookie, name='set_cookie'),
    path('get-coockie/', views.get_cookie, name='get_cookie'),
    
]