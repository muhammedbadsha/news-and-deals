from django.db import models

# Create your models here.
class Complaint(models.Model):
    name = models.CharField(db_column='Name', max_length=1000)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=1000)  # Field name made lowercase.
    subject = models.CharField(db_column='Subject', max_length=1000)  # Field name made lowercase.
    message = models.CharField(db_column='Message', max_length=1000)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    reply = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'complaint'
