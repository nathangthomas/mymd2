from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import ConditionSerializer
from .models import Condition

class ConditionViewSet(viewsets.ModelViewSet):
    queryset = Condition.objects.all().order_by('name')
    serializer_class = ConditionSerializer
