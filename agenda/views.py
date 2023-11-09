from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Contato
from django.http import Http404
from .serializer import EmailSerializer
from django.http import HttpResponse


def index(request):
    return HttpResponse("Olá mundo! Este é o app notes de Tecnologias Web do Insper.")


@api_view(['GET', 'POST'])
def agenda(request):
    try:
        email = Contato.objects.get(id=id)
    except Contato.DoesNotExist:
        raise Http404()
    
    if request.method == 'POST':
        new_email_data = request.data
        email.name = new_email_data['name']
        email.user = new_email_data['email']
        email.save()

    if request.method == 'GET':
        query_set = Contato.objects.all()
        serialized_email = EmailSerializer(query_set, many=True)
        return Response(serialized_email.data)

    serialized_email = EmailSerializer(email, many=True)
    return Response(serialized_email.data)

# vou acessar isso pela url 
@api_view(['GET'])
def agenda_detail(request, id):
    try:
        email = Contato.objects.get(id=id)

    except Contato.DoesNotExist:
        raise Http404()
    
    serialized_email = EmailSerializer(email, many=True)
    return Response(serialized_email.data)