#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

#主页(登入，注册系统待开发)
def index(request):
    return render(request,"index.html")

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