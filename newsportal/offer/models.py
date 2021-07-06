from django.db import models

# Create your models here.

class Offer(models.Model):
    sid = models.IntegerField()
    product_name = models.CharField(max_length=25)
    offer = models.CharField(max_length=25)
    shop_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'offer'

