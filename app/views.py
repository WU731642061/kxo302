#coding:utf-8
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from app.models import *

#主页
def index(request):
    user = request.user
    username = user.username
    if request.user.is_authenticated():
        userInfo = UserProfile.objects.get(user=user)
    return render(request,"index.html",locals())

@login_required(login_url='/')
def customer(request):
    if request.method == 'GET':
        user = request.user
        username = user.username
        userInfo = UserProfile.objects.get(user = user)
        print(userInfo.sex)
        return render(request,"customer.html",locals())
    if request.method == 'POST':
        errors = []
        user = request.user
        username = user.username
        userInfo = UserProfile.objects.get(user=user)
        password1 = request.POST.get('newpass')
        password2 = request.POST.get('repeatpass')

        gender = request.POST.get('gender')
        userphone = request.POST.get('phone')
        useremail = request.POST.get('email')

        if password1 != password2:
            errors.append("The password is different!")
            errors1 = errors[0]
            return render(request, "customer.html", locals())
        else:

            userInfo.sex = gender
            if userphone:
                userInfo.phone = userphone
            if useremail:
                user.email = useremail
            if password1 and password2 and password1==password2:
                print(password1)    #just for test
                user.set_password(password1)
            userInfo.save()
            user.save()
            return render(request,"customer.html", locals())

#只有level=1or2的人才能进的data management
@login_required(login_url='/')
def manage(request):
    if request.method == 'GET':
        user = request.user
        username = user.username
        if request.user.is_authenticated():
            userInfo = UserProfile.objects.get(user=user)
        shops = ShopInfo.objects.all()
        tags = shoptag.objects.all()
        return render(request, "manage.html",locals() )

#删除商铺，分类
def delpic(request):
    if request.method == 'POST':
        picID = request.POST.get('pic_id')  # 获取图片id值
        id = request.POST.get('shop_id')
        pic = shopPic.objects.get(id=picID)
        pic.delete()
        return HttpResponseRedirect("/manage/")

def deltag(request):
    if request.method == 'GET':
        id = request.GET['id']
        tag = shoptag.objects.get(id=id)
        tag.delete()
        return HttpResponseRedirect("/manage/")


def delshop(request):
    if request.method == 'GET':
        id = request.GET['id']
        shop = ShopInfo.objects.get(id=id)
        shop.delete()
        return HttpResponseRedirect("/manage/")


def newtag(request):
    if request.method == 'POST':

        shops = ShopInfo.objects.all()
        tags = shoptag.objects.all()

        errors = []
        name = request.POST.get('tagname')
        intro = request.POST.get('tagintro')
        img = request.FILES.get('tagpic')
        print(name,intro,img)
        if not name:
            errors.append("Please add tag name!")
            errors1 = errors[0]
            return render(request, "manage.html", locals())
        if not intro:
            errors.append("Please add tag introduction!")
            errors2 = errors[0]
            return render(request, "manage.html", locals())
        if errors == []:
            tag = shoptag()
            tag.tagname =name
            tag.tagIntro = intro
            tag.tagPic = img
            tag.save()
            return HttpResponseRedirect("/manage/")
    else:
        shops = ShopInfo.objects.all()
        tags = shoptag.objects.all()
        return render(request, "manage.html", locals())

def newshop(request):
    if request.method == 'POST':

        shops = ShopInfo.objects.all()
        tags = shoptag.objects.all()

        errors = []
        name =  request.POST.get('shopname')
        address = request.POST.get('shopaddress')
        introduction = request.POST.get('shopintro')
        tag = request.POST.get('access')
        cover = request.FILES.get('shoppic')
        if not name:
            errors.append("Please add shop name!")
            errors3 = errors[0]
            return render(request, "manage.html", locals())
        if not address:
            errors.append("Please add shop aadress!")
            errors4 = errors[0]
            return render(request, "manage.html", locals())
        if not introduction:
            errors.append("Please add shop introduction!")
            errors7 = errors[0]
            return render(request, "manage.html", locals())
        if not tag:
            errors.append("Please select shop tag!")
            errors5 = errors[0]
            return render(request, "manage.html", locals())

        shopCheck = ShopInfo.objects.filter(shopName=name)

        if len(shopCheck) > 0:
            errors.append("shop has existed")
            errors6 = errors[0]
            return render(request, "manage.html", locals())

        if errors == []:
            shop = ShopInfo()
            taginfo =shoptag.objects.get(tagname=tag)
            shop.shopName = name
            shop.shopAddress = address
            shop.shopIntro = introduction
            shop.shopCover = cover
            shop.tag = taginfo
            shop.save()
            return HttpResponseRedirect("/manage/")


    else:
        shops = ShopInfo.objects.all()
        tags = shoptag.objects.all()
        return render(request, "manage.html", locals())

@login_required(login_url='/')
def tagdetail(request):
    if request.method == 'GET':
        id = request.GET['id']
        tag = shoptag.objects.get(id = id)
        return render(request, "tagDetail.html", locals())
    else:
        errors = []
        id = request.POST.get('tagid')
        name = request.POST.get('tagname')
        intro = request.POST.get('tagintro')
        img = request.FILES.get('tagpic')
        print(name, intro, img)
        if not name:
            errors.append("Please add tag name!")
            errors1 = errors[0]
            return render(request, "tagDetail.html", locals())
        if not intro:
            errors.append("Please add tag introduction!")
            errors2 = errors[0]
            return render(request, "tagDetail.html", locals())
        if errors == []:
            tag = shoptag.objects.get(id=id)
            tag.tagIntro = intro
            if img:
                tag.tagPic = img
            tag.save()
            return HttpResponseRedirect("/manage/")

@login_required(login_url='/')
def shopdatail(request):
    if request.method == 'GET':
        id = request.GET['id']
        shop = ShopInfo.objects.get(id = id)
        tags = shoptag.objects.all()
        pic = shopPic.objects.filter(shop=shop)

        return render(request, "shopDetail.html",locals())
    else:
        errors = []
        id = request.POST.get('shopid')
        name = request.POST.get('shopname')
        address = request.POST.get('shopaddress')
        introduction = request.POST.get('shopintro')
        tag = request.POST.get('access')
        cover = request.FILES.get('shoppic')
        img = request.FILES.get('contentpic')

        shop = ShopInfo.objects.get(id=id)
        tags = shoptag.objects.all()
        pic = shopPic.objects.filter(shop=shop)

        if not name:
            errors.append("Please add shop name!")
            errors3 = errors[0]
            return render(request, "shopDetail.html", locals())
        if not address:
            errors.append("Please add shop address!")
            errors4 = errors[0]
            return render(request, "shopDetail.html", locals())
        if not introduction:
            errors.append("Please add shop introduction!")
            errors7 = errors[0]
            return render(request, "shopDetail.html", locals())
        if not tag:
            errors.append("Please select shop tag!")
            errors5 = errors[0]
            return render(request, "shopDetail.html", locals())


        if errors == []:
            taginfo = shoptag.objects.get(tagname=tag)
            shop.shopAddress = address
            shop.shopIntro = introduction
            if cover:
                shop.shopCover = cover
            if img:
                contentImg = shopPic()
                contentImg.shop = shop
                contentImg.shopPic = img
                contentImg.save()

            shop.tag = taginfo
            shop.save()
            return HttpResponseRedirect("/manage/")



def fish(request):
    return render(request,"fish.html")

def food(request):
    tags = shoptag.objects.all()
    return render(request,"food.html", locals())

def restaurant(request):
    name = request.GET['tag']
    tag = shoptag.objects.get(tagname=name)
    shop = ShopInfo.objects.filter(tag = tag)
    return render(request, "restaurant.html", locals())

def detail(request):
    id = request.GET['id']
    shop = ShopInfo.objects.get(id = id)
    pic = shopPic.objects.filter(shop=shop)
    return render(request, "detail.html", locals())

def future(request):
    return render(request,"future.html")

def healthy(request):
    return  render(request,"healthy.html")

def problems(request):
    return render(request,"problems.html")


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
        username = request.POST.get('log_username')
        password = request.POST.get('log_password')
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

