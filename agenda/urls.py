from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/emailsuser/', views.agenda, name='agenda'), #tds os emails
    
]