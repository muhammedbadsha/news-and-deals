from django.db import models




class Shop(models.Model):
    sid = models.AutoField(primary_key=True)
    logid = models.IntegerField()
    shop_name = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    status = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'shop'

