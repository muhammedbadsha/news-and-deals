from django.db import models

# Create your models here.
class Shop(models.Model):
    sid = models.IntegerField()
    shop_name = models.CharField(max_length=50)
    area_location = models.CharField(db_column='area/location', max_length=50)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'shop'

