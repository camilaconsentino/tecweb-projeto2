
# serializers.py
from rest_framework import serializers
from .models import Contato

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = ['id', 'name', 'email', 'send_time']