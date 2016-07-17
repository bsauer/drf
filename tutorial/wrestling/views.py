from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from .models import Promotion, Wrestler
from .serializers import WrestlerSerializer, PromotionSerializer

class PromotionView(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer 

class WrestlerView(viewsets.ModelViewSet):
    queryset = Wrestler.objects.all()
    serializer_class = WrestlerSerializer 

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        promotion_id = self.kwargs.get('promotion_pk', None)
        promotion_stat, created = PromoionStat.objects.get_or_create(promotion=promotion_id)
        promotion_stat.count += 1
        promotion_stat.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
