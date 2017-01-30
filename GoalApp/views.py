import json
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
# Create your views here.
from GoalApp.forms import LoginForm
from GoalApp.models import UserP


def login_view(request):
    f = LoginForm(request.POST)
    if request.method=='POST':
        if f.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            try:
                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request,user)
                    userprofile = UserP.objects.get(user=request.user)

                    return render(request,"GoalApp/home.html",{'user':userprofile.user})

                else:
                    return render(request, "GoalApp/login.html", { 'form': f, 'msg': 'user does not exist' })

            except ObjectDoesNotExist:
                return render(request, "GoalApp/login.html", { 'form': f, 'msg': '' })
        else:
            return render(request, "GoalApp/login.html", {'form':f ,'msg': 'validation error' })
            # resp={'status': 'failed','data': f.errors}
            # return HttpResponse(json.dumps(resp))
    f = LoginForm()
    return render(request, 'GoalApp/login.html',{'form':f})


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)




































































