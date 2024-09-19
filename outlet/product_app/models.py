from django.db import models
from account_app.models import Provider

class Product(models.Model):
    name = models.CharField(max_length=50)
    start_price = models.PositiveIntegerField()
    provider = models.ForeignKey(Provider , on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Auction(models.Model):
    title = models.CharField(max_length=50)
    product = models.OneToOneField(Product , on_delete=models.CASCADE)
    owner = models.ForeignKey(Product.provider , on_delete=models.CASCADE)
    start_date = models.DateField()
    start_time = models.TimeField()
    start_price = models.OneToOneField(Product.start_price , on_delete=models.CASCADE)
    active = models.BooleanField(defual= True)

    def __str__(self):
        return self.title
# Create your models here.
