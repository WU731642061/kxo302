#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request,"index.html")


