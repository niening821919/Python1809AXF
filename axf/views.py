from django.shortcuts import render

# Create your views here.
from axf.models import wheel, nav, mustbuy, shop, Mainshow, Foodtypes, Goods


def home(request): # 首页
    # 轮播图数据
    wheels = wheel.objects.all()

    # 导航数据
    navs = nav.objects.all()

    # 每日必购
    mustbuys = mustbuy.objects.all()

    # 商品部分
    shopList = shop.objects.all()
    shophead = shopList[0]
    shoptab = shopList[1:3]
    shopclass = shopList[3:7]
    shopcommend = shopList[7:11]

    # 商品主体内容
    mainshows = Mainshow.objects.all()

    data = {
        'wheels': wheels,
        'navs': navs,
        'mustbuys': mustbuys,
        'shophead': shophead,
        'shoptab': shoptab,
        'shopclass': shopclass,
        'shopcommend': shopcommend,
        'mainshows': mainshows,

    }

    return render(request, 'home/home.html', context=data)


def market(request, categoryid, childid, sortid):   # 闪购超市
    # 分类信息
    foodtypes = Foodtypes.objects.all()

    # 分类的点击下标
    typeIndex = int(request.COOKIES.get('typeIndex', 0))
    # 根据分类下标 获取 对应的 分类id
    categoryid = foodtypes[typeIndex].typeid

    # 子类信息
    childtypenames = foodtypes.get(typeid=categoryid).childtypenames

    childtypeList = []
    for item in childtypenames.split('#'):
        arr = item.split(':')
        dir = {
            'childname': arr[0],
            'childid': arr[1],
        }
        childtypeList.append(dir)

    # goodsList = Goods.objects.all()[0:5]
    if childid == '0':
        goodsList = Goods.objects.filter(categoryid=categoryid)
    else:
        goodsList = Goods.objects.filter(categoryid=categoryid, childcid=childid)

    # 排序
    if sortid == '1':
        goodsList = goodsList.order_by('productnum')
    elif sortid == '2':
        goodsList = goodsList.order_by('price')
    elif sortid == '3':
        goodsList = goodsList.order_by('marketprice')


    data = {
        'foodtypes': foodtypes,
        'goodsList': goodsList,
        'childtypeList': childtypeList,
        'categoryid': categoryid,
        'childid': childid,
    }


    return render(request, 'market/market.html', context=data)


def cart(request):
    return render(request, 'cart/cart.html')


def mine(request):
    return render(request, 'mine/mine.html')