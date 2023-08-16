from django.http import HttpResponse
from rest_framework import viewsets
from . import serializer, models

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.UserSerializer
    queryset = models.User.objects.all()