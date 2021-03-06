"""kxo302 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app import views as app_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns #导入CSS

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', app_view.index,name='index'),
    url(r'^contact/$', app_view.contact,name="contact"),
    url(r'^food/$', app_view.food,name='food'),
    url(r'^restaurant/$', app_view.restaurant,name='restaurant'),
    url(r'^detail/$', app_view.detail, name='detail'),
    url(r'^future/$', app_view.future, name='future'),
    url(r'^healthy/$', app_view.healthy, name='healthy'),
    url(r'^problems/$', app_view.problems, name='problems'),
    url(r'^suwu/$', app_view.suwu, name='suwu'),
    url(r'^tai/$', app_view.tai, name='tai'),


    #客户端
    url(r'^customer/$', app_view.customer, name='customer'),

    #管理端
    url(r'^manage/$', app_view.manage, name='manage'),

    #创建新店和新分类
    url(r'^newtag/$', app_view.newtag, name='newtag'),
    url(r'^newshop/$', app_view.newshop, name='newshop'),

    #tag详情
    url(r'^tagdetail/$', app_view.tagdetail, name='tagdetail'),
    url(r'^shopdetail/$', app_view.shopdatail, name='shopdetail'),

    #登入板块
    url(r'^signup/$',app_view.signup, name='signup'),
    url(r'^logout/$',app_view.userlogout, name='userlogout'),
    url(r'^login/$',app_view.userlogin, name='userlogin'),

    #删除图片，数据
    url(r'^delpic/$', app_view.delpic, name='delpic'),
    url(r'^deltag/$', app_view.deltag, name='deltag'),
    url(r'^delshop/$', app_view.delshop, name='delshop'),




]

urlpatterns += staticfiles_urlpatterns()