from django.shortcuts import render
from local_news.models import LocalNews
# Create your views here.
def postlocalnews(request):
    if request.method=="POST":
        obj=LocalNews()
        obj.news=request.POST.get('news')
        obj.area=request.POST.get('area')
        obj.date=request.POST.get('date')
        obj.time=request.POST.get('time')
        obj.save()
    return render(request,'local_news/localnws.html')
def viewlocalnews(request):
    ob=LocalNews.objects.all()
    context={
        'objval':ob,
    }

    return render(request,'local_news/viewlocalnws',context)

def viewslocalnews(request):
    ob=LocalNews.objects.all()
    context={
        'objval':ob,
    }

    return render(request,'local_news/subview.html',context)

def locaprrove(request,idd):
    ob=LocalNews.objects.get(id=idd)
    ob.status='active'
    ob.save()
    return viewslocalnews(request)

def locreject(request,idd):
    ob=LocalNews.objects.get(id=idd)
    ob.status='block'
    ob.save()
    return viewslocalnews(request)