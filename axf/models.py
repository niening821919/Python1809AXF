from django.db import models

# Create your models here.
class base(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=40)
    trackid = models.CharField(max_length=10)

    class Meta:
        abstract = True

# 轮播图
class wheel(base):
    class Meta:
        db_table = 'axf_wheel'


class nav(base):
    class Meta:
        db_table = 'axf_nav'


class mustbuy(base):
    class Meta:
        db_table = 'axf_mustbuy'



