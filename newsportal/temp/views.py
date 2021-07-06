from django.shortcuts import render
from channel_news.models import ChannelNews
# Create your views here.
def ind(request):
    return render(request,'temp/index.html')

def admin(request):
    return render(request,'temp/admin.html')

def subadmin(request):
    return render(request,'temp/subadmin.html')


def shop(request):
    return render(request,'temp/shop.html')

def channel(request):
    return render(request,'temp/channel.html')

def user(request):
    return render(request,'temp/user.html')

def search(request):

    return render(request,'user/search.html')
