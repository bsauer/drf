from .models import Promotion, Wrestler
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        #fields = ('name', 'place')

class WrestlerSerializer(serializers.ModelSerializer):
    promotion_id = serializers.PrimaryKeyRelatedField(
        queryset=Promotion.objects.all(),
        source='promotion',
        write_only=True
    )
    promotion = PromotionSerializer(read_only=True)
    class Meta:
        model = Wrestler
        fields = ('id', 'name', 'promotion', 'promotion_id')

    '''
    def create(self, vailidated_data):
        promotion_data = vailidated_data.pop('promotion')
        promotion = Promotion.objects.get(**promotion_data)
        wrestler = Wrestler.objects.create(promotion=promotion,
                                           **vaidated_data)
        return Wrestler
    '''

