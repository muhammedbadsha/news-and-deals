from django.shortcuts import render
from login.models import Login
from django.http import HttpResponseRedirect

# Create your views here.
def login(request):
    if request.method == "POST":
        uname = request.POST.get('usr')
        pssw = request.POST.get('name')
        # pas=sha256(pssw.encode()).hexdigest()
        obj = Login.objects.filter(username=uname, password=pssw)
        if obj:
            tp = ""
            for ob in obj:
                tp = ob.type
                uid = ob.uid

                if tp == "admin":
                    request.session['uid'] = uid
                    return HttpResponseRedirect("/temp/ad/")
                    # return render(request, 'temp/admin.html')

                elif tp == "shop":
                    request.session['uid'] = uid
                    return render(request, 'temp/shop.html')
                elif tp == "user":
                    request.session['uid'] = uid
                    # return render(request, 'temp/user.html')
                    return HttpResponseRedirect("/channelnews/channelnews1")

                elif tp == "channel":
                    request.session['uid'] = uid
                    return render(request, 'temp/channel.html')
                # elif tp == "user":
                #     request.session['uid'] = uid
                #     return render(request, 'login/subadmin_home.html')
                else:

                    objlist = "Username or password incorrect...please try again...!"
                    context = {
                        'msg': objlist,
                    }
                    return render(request, 'login/login.html', context)
        else:
            objlist = "Username or password incorrect...please try again...!"
            context = {
                'msg': objlist,
            }
            return render(request, 'login/login.html', context)
    return render(request, "login/login.html")

