from django.shortcuts import render
from shop.models import Shop
from login.models import Login
# Create your views here.
def postshop(request):
    if request.method=="POST":
        obj=Shop()
        obj.shop_name=request.POST.get('pnm')
        obj.area_location=request.POST.get('sn')
        obj.district=request.POST.get('district')
        obj.state=request.POST.get('stn')
        obj.phone_number=request.POST.get('ph')
        obj.password = request.POST.get('pwd')
        obj.save()

        ob = Login()
        ob.username = request.POST.get('pnm')
        ob.password = request.POST.get('pwd')
        ob.uid=obj.id
        ob.type="shop"
        ob.save()

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
