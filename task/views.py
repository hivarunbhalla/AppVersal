from django.shortcuts import render, HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import app
from .serializers import appSerializer, userdataSeriaizer

# Create your views here.
def home(request):
    return HttpResponse('Ok')

class appViewSet(ModelViewSet):
    queryset = app.objects.all()
    serializer_class = appSerializer


class userdataViewSet(ModelViewSet):
    serializer_class = userdataSeriaizer
    
    def get_queryset(self, *args, **kwargs):
        queryset = app.objects.filter(id = kwargs['pk'])
        