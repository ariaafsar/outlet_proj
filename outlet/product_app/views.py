from django.shortcuts import render
from .serializers import AuctionSerializer
from .models import Product , Auction
from rest_framework.generics import ListAPIView , CreateAPIView
from rest_framework.views import APIView



class AuctionList(ListAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer

class CreateAuction(CreateAPIView):
    serializer_class = AuctionSerializer
    def post(self , request , *args , **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        auction = serializer.save()
        auction_create = AuctionSerializer.objects.create(title = auction , )
class CancelAucton(APIView):
    def get (self,request):
        data = request.data(data = request.POST)
        if data['vaziat'] == False:
                    auction_create = Auction.objects.get(id = id_Aucton )
                    auction_create.Auction = True


