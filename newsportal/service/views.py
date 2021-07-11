from django.shortcuts import render
from service.models import Service
# Create your views here.
def postservice(request):
    if request.method=="POST":
        obj=Service()
        obj.service_category=request.POST.get('service')
        obj.service_name = request.POST.get('sn')
        obj.municipality_panjayath=request.POST.get('munipanch')
        obj.district=request.POST.get('district')
        obj.state=request.POST.get('state')
        obj.phone_number=request.POST.get('ph')
        obj.date=request.POST.get('date')
        obj.time=request.POST.get('time')
        obj.save()
    return render(request,'service/service.html')
def viewservice(request):
    if request.method=="POST":
        name=request.POST.get('service')
        ob = Service.objects.filter(service_category=name)
        context = {
            'objval': ob,
        }
        return render(request, 'service/viewservice.html', context)


    return render(request,'service/viewservice.html')
