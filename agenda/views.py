# from django.http import HttpResponse
# from rest_framework.decorators import api_view
# from .models import Contato
# from django.shortcuts import render, redirect
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import viewsets
# from .models import Contato
# from django.http import Http404, JsonResponse
# from .serializer import EmailSerializer
# from django.http import HttpResponse
# import requests
# from rest_framework.decorators import api_view
# import json

# def index(request):
#     return HttpResponse("Olá mundo! Este é o app notes de Tecnologias Web do Insper.")



# @api_view(['GET', 'POST'])
# def agenda(request):
#     if request.method == 'POST':
#         new_name = request.data.get('name')
#         new_email = request.data.get('email')

#         api_url = 'https://api.mailpro.com/v3/send/mail'
#         token = get_token()  # Supondo que você tenha uma função para obter o token

#         headers = {
#             'accept': 'application/json',
#                 'Content-Encoding': 'Encoding.UTF8',
#                 "Authorization": f"Bearer {token}",
#                 "Access-Control-Allow-Origin": "*",
#                 "Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,PATCH,OPTIONS",
#         }

#         email = {
#             "email": new_email,
#             "id_sender_email": 322291,
#             "body_html": f'Olá ${new_name}, bem vinde a nossa familia! Entre no site para marcar sua primeira aula',
#             "date_planned": None,
#             "subject": 'Bem Vinde!!',
#         }


#         response = requests.post(api_url, json=email, headers=headers)
#         #print(response.json())  

        
#         # Verifica se já existe um contato com o mesmo e-mail
#         if not Contato.objects.filter(email=new_email).exists():
#             new_contato = Contato(name=new_name, email=new_email)
#             new_contato.save()
#             return HttpResponse("Email cadastrado com sucesso!", status=201)
#         else:
#             return HttpResponse("Email já cadastrado.", status=400)

#     # Seu código para o método GET aqui (se necessário)

#     return HttpResponse("Método não suportado", status=405)

# @api_view(['POST'])
# def send_email_proxy(request):
#     api_url = 'https://api.mailpro.com/v3/send/mail'
#     token = get_token()  # Supondo que você tenha uma função para obter o token

#     headers = {
#         'accept': 'application/json',
#             'Content-Encoding': 'Encoding.UTF8',
#             "Authorization": f"Bearer {token}",
#             "Access-Control-Allow-Origin": "*",
#             "Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,PATCH,OPTIONS",
#     }


#     response = requests.post("https://api.mailpro.com/v3/send/mail", json=email_body, headers=headers)
#     #print(response.json())  

#     response = requests.post(api_url, headers=headers, json=request.data)
#     return JsonResponse(response.json(), status=response.status_code)

# def get_token():
#     print('get_token')
#     api_url = 'https://api.mailpro.com/v3/token'
#     data = {
#         'grant_type': 'password',
#         'username': 'mariavjs@al.insper.edu.br',
#         'password': '914af416-db21-4581-9a3f-dcd92b121676',
#     }
#     response = requests.post(api_url, data=data)
#     return response.json().get('access_token')


from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from .models import Contato
import requests
import json

def index(request):
    return HttpResponse("Olá mundo! Este é o app notes de Tecnologias Web do Insper.")


@api_view(['POST'])
def agenda(request):
    if request.method == 'POST':
        new_name = request.data.get('name')
        new_email = request.data.get('email')



        # Verifica se já existe um contato com o mesmo e-mail
        if not Contato.objects.filter(email=new_email).exists():
            new_contato = Contato(name=new_name, email=new_email)
            new_contato.save()

            # Chama a função para enviar e-mail
            send_email(new_name, new_email)

            return HttpResponse("Email cadastrado com sucesso!", status=201)
        
        elif new_email != None:
            return HttpResponse("Insira um Email.", status=400)
        
        else:
            return HttpResponse("Email já cadastrado.", status=400)

    # Seu código para o método GET aqui (se necessário)
    return HttpResponse("Método não suportado", status=405)

def send_email(name, email):
    token = get_token()

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }

    email_body = {
        'email': email,
        'id_sender_email': 322291,
        'body_html': f'Olá {name}, bem vinde a nossa familia! Entre no site para marcar sua primeira aula',
        'date_planned': None,
        'subject': 'Bem Vinde!!',
    }

    response = requests.post("https://api.mailpro.com/v3/send/mail", json=email_body, headers=headers)
    print(response.json())  # Opcional: Remova esta linha em produção

def get_token():
    api_url = 'https://api.mailpro.com/v3/token'
    data = {
        'grant_type': 'password',
        'username': 'mariavjs@al.insper.edu.br',  # Substitua com o seu nome de usuário
        'password': '914af416-db21-4581-9a3f-dcd92b121676',  # Substitua com a sua senha da API
    }
    response = requests.post(api_url, data=data)
    return response.json().get('access_token')

