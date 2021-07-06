"""newsportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [

    url(r'^channel/',include('channel.curl')),
    url(r'^channelnews/',include('channel_news.churl')),
    url(r'^complaint/',include('complaint.courl')),
    url(r'^localnews/',include('local_news.lnurl')),
    url(r'^offer/',include('offer.offurl')),
    url(r'^service/',include('service.serurl')),
    url(r'^shop/', include('shop.shourl')),
    url(r'^user/', include('user.suburl')),
    url(r'^login/',include('login.lourl')),
    url(r'^temp/',include('temp.url')),


]
urlpatterns+=staticfiles_urlpatterns()