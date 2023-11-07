
# serializers.py
from rest_framework import serializers
from .models import Agenda

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = ['id', 'name', 'email', 'send_time']