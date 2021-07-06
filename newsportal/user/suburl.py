from  django.conf.urls import url
from user import views
urlpatterns=[
    url(r'^user/',views.postuser),
    url(r'^vuser/',views.viewuser),
    # url(r'^search/',views.search),
    # url('approve/(?P<idd>\w+)',views.aprrove,name='approve'),
    # url('reject/(?P<idd>\w+)',views.reject,name='reject')
]