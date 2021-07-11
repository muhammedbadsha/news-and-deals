from django.db import models

# Create your models here.
class Service(models.Model):
    service_category = models.CharField(max_length=50)
    service_name = models.CharField(max_length=50)
    municipality_panjayath = models.CharField(db_column='municipality/panjayath', max_length=50)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'service'

