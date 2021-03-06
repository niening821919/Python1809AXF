import hashlib
import os
import uuid

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from Python1809AXF import settings
from axf.models import wheel, nav, mustbuy, shop, Mainshow, Foodtypes, Goods, User


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
    # 获取用户信息
    token = request.session.get('token')

    responseData = {

    }

    if token: # 登录
        user = User.objects.get(token=token)
        responseData['name'] = user.name
        responseData['rank'] = user.rank
        responseData['img'] = '/static/uploads/' + user.img
        responseData['isLogin'] = 1
    else:
        responseData['name'] = '未登录'
        responseData['img'] = '/static/uploads/axf.png/'


    return render(request, 'mine/mine.html', context=responseData)


def genarate_password(param):
    sha = hashlib.sha256()
    sha.update(param.encode('utf-8'))
    return sha.hexdigest()

def registe(request):
    if request.method == 'GET':
        return render(request, 'mine/registe.html')
    elif request.method == 'POST':
        user = User()
        user.account = request.POST.get('account')
        user.password = genarate_password(request.POST.get('password'))
        user.name = request.POST.get('name')
        user.phone = request.POST.get('phone')
        user.addr = request.POST.get('addr')
        # user.img = 'axf.png'

        imgName = user.account + '.png'
        imagePath = os.path.join(settings.MEDIA_ROOT, imgName)
        file = request.FILES.get('icon')
        with open(imagePath, 'wb') as fp:
            for data in file.chunks():
                fp.write(data)
        user.img = imgName

        user.token = str(uuid.uuid5(uuid.uuid4(), 'register'))

        user.save()

        request.session['token'] = user.token

        return redirect('axf:mine')


def checkaccount(request):
    account = request.GET.get('account')
    responseData = {
        'msg': '账号可用',
        'status': 1
    }
    try:
        user = User.objects.get(account=account)
        responseData['msg'] = '账号已被占用'
        responseData['status'] = -1
        return JsonResponse(responseData)
    except:
        return JsonResponse(responseData)


def logout(request):
    request.session.flush()
    return redirect('axf:mine')


def login(request):
    if request.method == 'GET':
        return render(request, 'mine/login.html')
    elif request.method == 'POST':
        account = request.POST.get('account')
        password = request.POST.get('password')

        try:
            user = User.objects.get(account=account)
            if user.password == genarate_password(password):
                # 更新token
                token = str(uuid.uuid5(uuid.uuid4(), 'login'))
                user.save()
                request.session['token'] = user.token
                return redirect('axf:mine')
            else:
                return render(request, 'mine/login.html', context={'passwordErr': '密码错误!'})
        except:
            return render(request, 'mine/login.html', context={'accountErr': '账号不存在！'})