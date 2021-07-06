from django.conf.urls import url
from channel_news import views
urlpatterns=[
    url(r'^channelnews/',views.viewchannel),
    url(r'^channelnews1/',views.viewchannel_news),
    url(r'^manage/',views.managechannelnews),
    url(r'^ddelete/(?P<idd>\w+)', views.channeldelete, name='ddelete'),
    url(r'^smore/(?P<idd>\w+)', views.smore, name='smore'),
]