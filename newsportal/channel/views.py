from django.shortcuts import render
from channel.models import Channel
from channel_news.models import ChannelNews
from login.models import Login
from channel_news.models import ChannelNews

from django.http import HttpResponse
# Create your views here.
def view_channel(request):
    if request.method=="POST":
        obj=Channel()
        obj.logid=1
        obj.name=request.POST.get('nm')
        obj.location=request.POST.get('loc')
        obj. municipality_panjayath=request.POST.get('plc')
        obj.district=request.POST.get('district')
        obj.state=request.POST.get('stn')
        obj.pin=request.POST.get('pin')
        obj.phone_number=request.POST.get('ph')
        obj.password = request.POST.get('pwd')
        obj.status="pending"
        obj.save()



    return render(request, 'channel/post channel.html')

def viewchannel(request):
    ob=Channel.objects.all()
    context ={
        'objval':ob,
    }
    return render(request,'channel/channel.html',context)
def chaprrove(request,idd):
    obj=Channel.objects.get(c_id=idd)
    obj.status='active'
    obj.save()

    ob=Login()
    ob.username = obj.name
    ob.password = obj.password
    ob.uid = obj.c_id
    ob.type = "channel"
    ob.save()
    return viewchannel(request)
def chreject(request,idd,iid):
    ob=Channel.objects.get(c_id=idd)
    ob.status='block'
    ob.save()
    ob=Login.objects.get(uid=iid)
    ob.type='block'
    ob.save()

    return viewchannel(request)

def vuserchannel(request):
    ob=Channel.objects.filter(status='active')
    context ={
        'objval':ob,
    }
    return render(request,'channel/userchannel.html',context)
def more(request):
    u=str(request.session['uid'])
    ob = ChannelNews.objects.get(id=u)
    context={
        'val':ob,
    }
    # return viewchannel(request)
    return render(request,'channel_news/view_news_by.html',context)