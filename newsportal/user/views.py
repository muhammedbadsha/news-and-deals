from django.shortcuts import render
from user.models import User
from login.models import Login
from channel_news.models import ChannelNews
# Create your views here.
def postuser(request):
    if request.method=="POST":
        obj=User()
        obj.logid=1
        obj.name=request.POST.get('nm')
        obj.email=request.POST.get('email')
        obj.phone_number=request.POST.get('ph')
        obj.password = request.POST.get('pwd')
        obj.status='pending'
        obj.save()

        ob=Login()
        ob.username=request.POST.get('nm')
        ob.password=request.POST.get('pwd')
        ob.uid = obj.id
        ob.type = "user"
        ob.save()

    return render(request, 'user/usrreg.html')
def viewuser(request):
    ob=User.objects.all()
    context ={
        'objval':ob,
    }
    return render(request, 'user/usrreg.html', context)


def search(request):
    if request.method=='POST':
        ar=request.POST.get('s')
        ob=ChannelNews.objects.filter(area__contains=ar)
        context={
            'val':ob,
        }
        return render(request, 'user/search.html',context)
    return render(request,'user/search.html')

# def aprrove(request,idd):
#     ob=Subadmin.objects.get(id=idd)
#     ob.status='active'
#     ob.save()
#     return viewsubadmin(request)
# def reject(request,idd):
#     ob=Subadmin.objects.get(id=idd)
#     ob.status='block'
#     ob.save()
#     return viewsubadmin(request)