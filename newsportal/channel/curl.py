from django.conf.urls import url
from channel import views

urlpatterns=[
    url(r'^channel/', views.view_channel),
    url(r'^channel1/',views.viewchannel),
    url(r'^vuserchannel/',views.vuserchannel,name='vuserchannel'),
    url('chapprove/(?P<idd>\w+)',views.chaprrove,name='chapprove'),
    url('chreject/(?P<idd>\w+) (?P<iid>\w+)',views.chreject,name='chreject'),
    # url('more/',views.more,name='more'),
]
