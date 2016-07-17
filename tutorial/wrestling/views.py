from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Promotion, Wrestler
from .serializers import WrestlerSerializer, PromotionSerializer

class WrestlerView(viewsets.ModelViewSet):
    queryset = Wrestler.objects.all()
    serializer_class = WrestlerSerializer 

class PromotionView(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer 

