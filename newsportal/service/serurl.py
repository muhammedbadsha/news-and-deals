from django.conf.urls import url
from service import views
urlpatterns=[
    url(r'^service/',views.postservice),
    url(r'^vservice/',views.viewservice),
    url(r'^ind/',views.viewservice),
]