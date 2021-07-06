from django.shortcuts import render
from complaint.models import Complaint
import datetime
# Create your views here.
def  postcomplaint(request):
    if request.method=="POST":
        obj=Complaint()
        obj.name=request.POST.get('name')
        obj.email=request.POST.get('email')
        obj.subject=request.POST.get('subject')
        obj.message=request.POST.get('message')
        obj.date=datetime.date.today()
        obj.time=datetime.datetime.now().time()
        obj.reply = 'pending'
        obj.save()
    return render(request,'complaint/post complaint.html')


def viewcomplaint(request):
    ob=Complaint.objects.filter(reply='pending')
    context={
        'objval':ob,
    }
    return render(request,'complaint/viewcomplaint.html',context)


def rcomplaint(request,idd):
    ob=Complaint.objects.filter(id=idd)
    context={
        'objval':ob,
    }

    if request.method=="POST":
        ob=Complaint.objects.get(id=idd)
        ob.reply=request.POST.get('rply')
        ob.save()
    return render(request,'complaint/complaintreply.html',context)