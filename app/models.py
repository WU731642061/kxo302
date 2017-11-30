from django.db import models
from django.contrib.auth.models import User

#用户数据库

class UserProfile(models.Model):

    LEVELS = (
        (1, 'owner'),
        (2, 'manager'),
        (3, 'user'),
    )

    user = models.OneToOneField(User,unique=True, verbose_name=('用户'))
    level = models.IntegerField(default=3, choices=LEVELS)



#商店数据库



