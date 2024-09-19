from rest_framework import serializers
from .models import Auction , Product

class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = '__all__'

class CancelSeralzer(serializers.ModelSerializer):
    class Meta:
        model = Auction 
        fields = 'active'

    def create(self , validated_data):
        auction = Auction.objects.create(
            title = validated_data['title'],
            product = validated_data['product'],
            start_date = validated_data['start_data'],
            start_time = validated_data['start_time'],
            start_price = validated_data['start_price'],
        )
        return auction
