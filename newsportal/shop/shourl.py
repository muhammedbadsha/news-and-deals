from  django.conf.urls import url
from shop import views
urlpatterns=[
    url(r'^shop/',views.postshop),
    url(r'^vshop/',views.viewshop),
]