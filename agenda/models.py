from django.db import models

class Agenda(models.Model):
    title = models.CharField(max_length=200)