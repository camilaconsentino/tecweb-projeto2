from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Agenda
from django.http import Http404
from .serializer import EmailSerializer
from django.http import HttpResponse


def index(request):
    return HttpResponse("Olá mundo! Este é o app notes de Tecnologias Web do Insper.")


@api_view(['GET', 'POST'])
def agenda(request):
    try:
        email = Agenda.objects.get(id=id)
    except Agenda.DoesNotExist:
        raise Http404()
    
    if request.method == 'POST':
        new_email_data = request.data
        email.name = new_email_data['name']
        email.user = new_email_data['email']
        email.data = new_email_data['send_time']
        email.save()

    if request.method == 'GET':
        query_set = Agenda.objects.all()
        serialized_email = EmailSerializer(query_set, many=True)
        return Response(serialized_email.data)

    serialized_email = EmailSerializer(email, many=True)
    return Response(serialized_email.data)

# vou acessar isso pela url 
@api_view(['GET'])
def agenda_detail(request, id):
    try:
        email = Agenda.objects.get(id=id)

    except Agenda.DoesNotExist:
        raise Http404()
    
    serialized_email = EmailSerializer(email, many=True)
    return Response(serialized_email.data)