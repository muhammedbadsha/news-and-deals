from django.db import models
from channel.models import Channel
# Create your models here.



class ChannelNews(models.Model):
    # c_id = models.IntegerField()
    c=models.ForeignKey(Channel,to_field='c_id',on_delete=models.CASCADE)
    image = models.CharField(max_length=1000)
    title = models.CharField(max_length=100)
    news = models.CharField(max_length=2000)
    area = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    status = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'channel_news'

