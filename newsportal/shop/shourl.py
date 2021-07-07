from  django.conf.urls import url
from shop import views
urlpatterns=[
    url(r'^shop/',views.postshop),
    url(r'^vshop/',views.viewshop),
    url(r'^shop1/',views.view_shop),
    url('shapprove/(?P<idd>\w+)', views.shaprrove, name='shapprove'),
    url('shreject/(?P<idd>\w+) (?P<iid>\w+)', views.shreject, name='shreject'),

]