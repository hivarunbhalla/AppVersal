from rest_framework import serializers
from .models import app

class appSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = app
        fields = ['name', 'email', 'img']
        
class userdataSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = app
        fields = ['img']