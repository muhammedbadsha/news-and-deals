from django.shortcuts import render
from local_news.models import LocalNews
from channel_news.models import ChannelNews
# Create your views here.
def postlocalnews(request):
    if request.method=="POST":
        info=LocalNews()
        info.news=request.POST.get('news')
        info.area=request.POST.get('area')
        info.date=request.POST.get('date')
        info.time=request.POST.get('time')
        info.save()
    return render(request,'local_news/localnws.html')
def viewlocalnews(request):
    info=LocalNews.objects.all()
    context={
        'objval':info,
    }

    return render(request,'channel_news/viewchannelnws.html',context)

def viewslocalnews(request):
    info=LocalNews.objects.all()
    context={
        'objval':info,
    }

    return render(request,'channel_news/viewchannelnws.html',context)

# def locaprrove(request,idd):
#     ob=LocalNews.objects.get(id=idd)
#     ob.status='active'
#     ob.save()
#     return viewslocalnews(request)
#
# def locreject(request,idd):
#     ob=LocalNews.objects.get(id=idd)
#     ob.status='block'
#     ob.save()
#     return viewslocalnews(request)