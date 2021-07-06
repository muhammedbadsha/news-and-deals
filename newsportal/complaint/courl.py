from django.conf.urls import url
from complaint import views
urlpatterns=[
    url(r'^complaint/',views.postcomplaint),
    url(r'^vcomplaint/',views.viewcomplaint),
    url(r'^rcomplaint/(?P<idd>\w+)', views.rcomplaint, name='rcomplaint'),
]


