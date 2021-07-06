from django.db import models


class LocalNews(models.Model):
    news = models.CharField(max_length=2000)
    area = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'local_news'
