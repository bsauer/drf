from __future__ import unicode_literals

from django.db import models


class Promotion(models.Model):
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=50)


class Wrestler(models.Model):
    name = models.CharField(max_length=50)
    promotion = models.ForeignKey(Promotion)

class PromotionStat(models.Model):
    count = models.IntegerField(default=0)
    promotion = models.ForeignKey(Promotion)
