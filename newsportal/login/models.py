from django.db import models

# Create your models here.

class Login(models.Model):
    uid = models.IntegerField()
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=8)
    type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'login'
