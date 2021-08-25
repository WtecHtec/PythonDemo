from django.db import models

# Create your models here.
class Shopp(models.Model):
    shop_name = models.TextField(max_length=200)
    shop_price = models.IntegerField(default=0)
    shop_dsc = models.CharField(max_length=200)