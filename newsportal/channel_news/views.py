from django.shortcuts import render
from channel_news.models import ChannelNews
from channel.models import Channel
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
# Create your views here.
def viewchannel(request):
    if request.method=="POST":
        obj=ChannelNews()
        obj.news=request.POST.get('news')
        obj.area=request.POST.get('area')
        obj.date=request.POST.get('date')
        obj.time=request.POST.get('time')
        obj.status='pending'
        obj.c_id = request.session['uid']
        obj.title = request.POST.get('t')
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.image = myfile.name
        obj.save()
    return render(request, 'channel_news/channel news.html')


def viewchannel_news(request):
    # o=Channel.objects.all()
    ob=ChannelNews.objects.filter(status='pending')
    context={
        'objval':ob,
    }
    if request.method == 'POST':
        ar = request.POST.get('s')
        ob = ChannelNews.objects.filter(area__contains=ar)
        context = {
            'val': ob,
        }
        return render(request, 'user/search.html', context)
    return render(request,'channel_news/viewchannelnws.html',context)

def managechannelnews(request):
    ob=ChannelNews.objects.all()
    context={
        'objval':ob,
    }
    return render(request,'channel_news/managechannelnws.html',context)


def channeldelete(request,idd):
    ob = ChannelNews.objects.get(id=idd)
    ob.status ="deleted"
    ob.save()
    return managechannelnews(request)


def smore(request,idd):
    obj = ChannelNews.objects.filter(c_id=idd)
    # print(len(obj))
    context = {
        'val':obj
    }
    return render(request,'channel_news/view_news_by.html',context)


