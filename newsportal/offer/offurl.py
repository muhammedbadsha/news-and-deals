from  django.conf.urls import url
from offer import views
urlpatterns=[
    url(r'^offer/',views.postoffer),
    url(r'^voffer/',views.viewoffer),
    url(r'^shop/',views.postoffer),
    url(r'^shop/',views.viewoffer),
    url(r'^moffer/',views.manageoffer),
    url(r'^update/(?P<idd>\w+)', views.update, name='update'),
    url(r'^odelete/(?P<idd>\w+)', views.odelete, name='odelete'),
    url(r'^more/(?P<idd>\w+)', views.omore, name='omore'),
]