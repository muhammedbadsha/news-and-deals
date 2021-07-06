from  django.conf.urls import url
from temp import views
urlpatterns=[
    url(r'^ind/',views.ind),
    url(r'^ad/', views.admin),
    url(r'^sad/', views.subadmin),
    url(r'^shop/', views.shop),
    url(r'^channel/',views.channel),
    url(r'^user/',views.user),
    url(r'^srch/',views.search),


]