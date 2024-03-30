from django.urls import path
from . import views

urlpatterns = [
    
    path('set-session/', views.set_session, name='set_session'),
    path('get-session/', views.get_session, name='get_session'),
    
]