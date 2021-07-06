from django.conf.urls import url
from local_news import views
urlpatterns=[
    url(r'^localnews/',views.postlocalnews),
    url(r'^vlocalnews/',views.viewlocalnews),
    url(r'^subnews/', views.viewslocalnews),
    url(r'^approve/(?P<idd>\w+)', views.locaprrove,name="approve"),
    url(r'^reject/(?P<idd>\w+)', views.locreject,name="reject"),
]