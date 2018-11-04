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


# 导航
class nav(base):
    class Meta:
        db_table = 'axf_nav'


# 每日必购
class mustbuy(base):
    class Meta:
        db_table = 'axf_mustbuy'


class shop(base):
    class Meta:
        db_table = 'axf_shop'


# 商品主题内容
class Mainshow(models.Model):
    trackid = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    categoryid = models.CharField(max_length=100)
    brandname = models.CharField(max_length=50)

    img1 = models.CharField(max_length=100)
    childcid1 = models.CharField(max_length=10)
    productid1 = models.CharField(max_length=10)
    longname1 = models.CharField(max_length=100)
    price1 = models.FloatField()
    marketprice1 = models.FloatField()

    img2 = models.CharField(max_length=100)
    childcid2 = models.CharField(max_length=10)
    productid2 = models.CharField(max_length=10)
    longname2 = models.CharField(max_length=100)
    price2 = models.FloatField()
    marketprice2 = models.FloatField()

    img3 = models.CharField(max_length=100)
    childcid3 = models.CharField(max_length=10)
    productid3 = models.CharField(max_length=10)
    longname3 = models.CharField(max_length=100)
    price3 = models.FloatField()
    marketprice3 = models.FloatField()

    class Meta:
        db_table = 'axf_mainshow'


class Foodtypes(models.Model):
    typeid = models.CharField(max_length=8)
    typename = models.CharField(max_length=100)
    childtypenames = models.CharField(max_length=256)
    typesort = models.IntegerField()

    class Meta:
        db_table = 'axf_foodtypes'


class Goods(models.Model):
    productid = models.CharField(max_length=10)  # 商品ID
    productimg = models.CharField(max_length=100)  # 商品图片
    productname = models.CharField(max_length=100)  # 商品名称
    productlongname = models.CharField(max_length=100)  # 商品弄名称
    isxf = models.BooleanField(default=False)  # 精选
    pmdesc = models.BooleanField(default=False)  # 买一送一
    specifics = models.CharField(max_length=100)  # 规格
    price = models.DecimalField(max_digits=7, decimal_places=2)  # 价格
    marketprice = models.DecimalField(max_digits=7, decimal_places=2)  # 商场价格
    categoryid = models.IntegerField()  # 分类ID
    childcid = models.IntegerField()  # 子类ID
    childcidname = models.CharField(max_length=100)  # 分类名称
    dealerid = models.CharField(max_length=10)  # 详情ID
    storenums = models.IntegerField()  # 库存
    productnum = models.IntegerField()  # 销量

    class Meta:
        db_table = 'axf_goods'
