from django.db import models

# Create your models here.


class User(models.Model):
    logid = models.IntegerField()
    name = models.CharField(db_column='NAME', max_length=20)  # Field name made lowercase.
    email = models.CharField(max_length=50)
    phone_number = models.CharField(db_column='phone number', max_length=15)  # Field renamed to remove unsuitable characters.
    password = models.CharField(max_length=50)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'user'
