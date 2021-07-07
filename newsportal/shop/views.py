from django.shortcuts import render
from shop.models import Shop
from login.models import Login
from offer.models import Offer
# Create your views here.
def postshop(request):
    if request.method=="POST":
        obj=Shop()
        obj.logid=1
        obj.shop_name=request.POST.get('pnm')
        obj.area_location=request.POST.get('sn')
        obj.district=request.POST.get('dis')
        obj.state=request.POST.get('stn')
        obj.phone_number=request.POST.get('ph')
        obj.password = request.POST.get('pwd')
        ob = Login()
        ob.username = request.POST.get('pnm')
        ob.password = request.POST.get('pwd')
        ob.uid=obj.logid
        ob.type="shop"
        obj.save()

    return render(request,'shop/shop.html')
def viewshop(request):

    if request.method=="POST":
        dis=request.POST.get('dis')
        # ob = Shop.objects.all()

        obj = Shop.objects.filter(district=dis)
        context = {
            # 'objval': ob,
            'val': obj,

        }
        return render(request, 'shop/viewshop.html', context)
    else:
        ob = Shop.objects.all()
        context = {
            'val': ob,
        }

        return render(request, 'shop/viewshop.html', context)
    return render(request,'shop/viewshop.html')


def view_shop(request):
    ob=Shop.objects.all()
    context ={
        'val':ob,
    }
    return render(request,'shop/shopmanage.html',context)
def shaprrove(request,idd):
    obj=Shop.objects.get(sid=idd)
    obj.status='active'
    obj.save()

    ob=Login()
    ob.username = obj.shop_name
    ob.password = obj.password
    ob.uid = obj.sid
    ob.type = "shop"
    ob.save()
    return view_shop(request)

def shreject(request,idd,iid):
    ob=Shop.objects.get(sid=idd)
    ob.status='block'
    ob.save()
    ob=Login.objects.filter(uid=iid)
    ob.type='block'
    ob.save()

    return view_shop(request)


def vusershop(request):
    ob=Shop.objects.filter(status='active')
    context ={
        'objval':ob,
    }
    return render(request,'shop/viewshop.html',context)


def more(request,idd):
    ob = Offer.objects.filter(sid=idd)
    # print(len(obj))
    context = {
        'ob':ob
    }
    return render(request,'offer/viewoffer_by.html',context)
