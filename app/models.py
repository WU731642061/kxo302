from django.db import models
from django.contrib.auth.models import User

#用户数据库

class UserProfile(models.Model):

    LEVELS = (
        (1, 'owner'),
        (2, 'manager'),
        (3, 'user'),
    )

    SEX = (
            ('male','male'),
            ('female','female')
    )

    user = models.OneToOneField(User,unique=True, verbose_name=('用户'))
    phone = models.CharField(max_length=20, blank=True)
    sex = models.CharField(blank=True, null=True, default="male", choices=SEX, max_length=10)
    level = models.IntegerField(default=3, choices=LEVELS)




#商店数据库

class ShopInfo(models.Model):

    shopName = models.CharField(max_length=50,unique=True,blank=False,null=False)
    shopAddress = models.CharField(max_length=50)
    shopCover = models.ImageField(upload_to='cover', blank=True, null=True)  # 上传商铺封面图
    shopPic = models.ImageField(upload_to='picture', blank=True, null=True) #上传展示图片




