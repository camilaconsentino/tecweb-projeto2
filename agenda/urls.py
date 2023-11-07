from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/emailsuser', views.agenda, name='agenda'), #tds os emails
    path('api/emailsuser/<int:id>', views.agenda_detail, name='agenda_detail'), #email especifico
]