# models.py
from django.db import models

class Agenda(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    send_time = models.DateTimeField()