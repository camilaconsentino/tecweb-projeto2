# models.py
from django.db import models

class Contato(models.Model):
    #id = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=100)
    email = models.EmailField(default="")
    #send_time = models.DateTimeField()