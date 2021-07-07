from django.shortcuts import render
from offer.models import Offer
from shop.models import Shop
# Create your views here.
def postoffer(request):
    if request.method=="POST":
        obj=Offer()
        obj.sid = request.session['uid']
        obj.product_name=request.POST.get('pname')
        obj.offer=request.POST.get('offer')
        obj.shop_name=request.POST.get('sname')
        obj.location=request.POST.get('loc')
        obj.phone_number=request.POST.get('ph')
        obj.status="pending"
        obj.save()
    return render(request,'offer/offer.html')
def viewoffer(request):
    ob=Offer.objects.all()
    context={
        'objval':ob,
    }

    return render(request,'offer/viewoffer.html',context)

def manageoffer(request):
    ob=Offer.objects.all()
    context={
        'objval':ob,
    }

    return render(request,'offer/manageoffer.html',context)
#
def odelete(request, idd):
    obj= Offer()
    obj.id=idd
    obj.delete()
    return manageoffer(request)

def update(request,idd):
    ob = Offer.objects.get(id=idd)
    context = {
        'objval': ob,
    }
    if request.method == "POST":
        obj = Offer.objects.get(id=idd)
        obj.product_name = request.POST.get('pname')
        obj.offer = request.POST.get('offer')
        obj.shop_name = request.POST.get('sname')
        obj.location = request.POST.get('loc')
        obj.phone_number = request.POST.get('ph')
        obj.save()
        return manageoffer(request)
    return render(request, 'offer/update.html',context)



def omore(request,idd):
    ob = Offer.objects.filter(sid=idd)
    # print(len(obj))
    context = {
        'ob':ob
    }
    return render(request,'offer/viewoffer_by.html',context)
