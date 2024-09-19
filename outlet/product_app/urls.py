from django.urls import path
from .models import Product , Auction
from .views import AuctionList 

urlpatterns = [
    path('auctionlist' , AuctionList.as_view())
]