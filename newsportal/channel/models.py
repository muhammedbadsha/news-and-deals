from django.db import models

# Create your models here.



class Channel(models.Model):
    c_id = models.AutoField(primary_key=True)
    logid = models.IntegerField()
    name = models.CharField(db_column='NAME', max_length=20)  # Field name made lowercase.
    location = models.CharField(max_length=50)
    municipality_panjayath = models.CharField(db_column='municipality/panjayath', max_length=50)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    pin = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=50)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'channel'
