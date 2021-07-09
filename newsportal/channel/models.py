from django.db import models

# Create your models here.



class Channel(models.Model):
    c_id = models.AutoField(primary_key=True)
    logid = models.IntegerField()
    name = models.CharField(db_column='NAME', max_length=20)  # Field name made lowercase.
    location = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    email = models.CharField(max_length=1000)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=50)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'channel'

