#coding:utf-8
from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from app.models import *

#主页(登入，注册系统待开发)
def index(request):
    return render(request,"index.html")


def customer(request):
    if request.method == 'GET':
        user = request.user
        username = user.username
        userInfo = UserProfile.objects.filter(user = username)
        return render(request,"customer.html",locals())
    else:

        return render(request,"customer.html")

def fish(request):
    return render(request,"fish.html")

def food(request):
    return render(request,"food.html")

def future(request):
    return render(request,"future.html")

def healthy(request):
    return  render(request,"healthy.html")

def problems(request):
    return render(request,"problems.html")

def single(request):
    return render(request,"single.html")

def suwu(request):
    return render(request,"suwu.html")

def tai(request):
    return  render(request,"tai.html")

def contact(request):
    return  render(request,"contact.html")

#登入板块
#-----------------------------
#包括注册，登入，登出三个方法，无具体页面，均在index.html进行操作
#-----------------------------

def signup(request):
    if request.method == 'POST':
        if request.user.is_authenticated():
            return HttpResponseRedirect("/")
        else:
            username = request.POST.get('sign_username', '')
            email = request.POST.get('sign_email', '')
            password = request.POST.get('sign_password', '')
            errors = []

            if not username:
                print("没有用户名")
                errors.append("Please enter username!")
                return render(request, "index.html", {'errors1': errors[0]})

            if not email:
                print("没有邮箱")
                errors.append("Please enter email!")
                return render(request, "index.html", {'errors2': errors[0]})

            if not password:
                print("没有密码")
                errors.append("Please enter password!")
                return render(request, "index.html", {'errors3': errors[0]})

            userCheck = User.objects.filter(username=username)

            if len(userCheck) > 0:
                print("用户名错误")
                errors.append("The user has existed")
                return render(request, "index.html", {'errors4': errors[0]})

            if errors == []:
                user = User()
                user.username = username
                user.set_password(password)
                user.email = email
                user.save()
                # 用户扩展信息 profile
                profile = UserProfile()
                profile.user = user
                profile.save()

            newUser = auth.authenticate(username=username, password=password)
            if newUser is not None:
                auth.login(request, newUser)
                return HttpResponseRedirect("/")

def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('log_username', '')
        password = request.POST.get('log_password', '')
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect("/")
        else:
            result = '<span>Username or password is wrong, please input it again.</span>'
            return render(request, "index.html", {'result': result})

def userlogout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

