from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse

from app.models import MainWheel, MainNav, MainMustBuy, \
    MainShop, MainShow, FoodType, Goods, CartModel, \
    OrderModel, OrderGoodsModel
from utils.functions import get_order_num


def home(request):
    '''
    首页视图函数
    '''
    if request.method == 'GET':
        mainwheels = MainWheel.objects.all()
        mainnavs = MainNav.objects.all()
        mainbuys = MainMustBuy.objects.all()
        mainshops = MainShop.objects.all()
        mainshows = MainShow.objects.all()

        data = {
            'title': '首页',
            'mainwheels': mainwheels,
            'mainnavs': mainnavs,
            'mainbuys': mainbuys,
            'mainshops': mainshops,
            'mainshows': mainshows,
        }
        return render(request, 'home/home.html', data)


def market(request):
    if request.method == 'GET':
        return HttpResponseRedirect(reverse('axf:marketparams',
                                            kwargs={'typeid': 104749,
                                                    'sort_id': 0,
                                                    'child_id': 0}))


def marketparams(request, typeid, sort_id, child_id):
    if request.method == 'GET':
        foodtypes = FoodType.objects.all()

        if child_id:
            goods = Goods.objects.filter(categoryid=typeid,
                                         childcid=child_id)
        goods = Goods.objects.filter(categoryid=typeid)
        childtypenames = FoodType.objects.filter(typeid=typeid).first().childtypenames
        if childtypenames:
            childtypenames_list = [i.split(':') for i in childtypenames.split('#')]

            if sort_id == '0':
                pass
            elif sort_id == '1':
                goods = goods.order_by('productnum')

            elif sort_id == '2':
                goods = goods.order_by('-price')

            elif sort_id == '3':
                goods = goods.order_by('price')

            data = {
                'foodtypes': foodtypes,
                'goods': goods,
                'typeid': typeid,
                'sort_id': sort_id,
                'child_id': child_id,
                'childtypenames_list': childtypenames_list
            }
            return render(request, 'market/market.html', data)


def add_to_cart(request):
    if request.method == 'POST':
        user = request.user
        goods_id = request.POST.get('goods_id')

        data = {
            'code': 200,
            'msg': '请求成功',
        }

        if user.id:
            cart = CartModel.objects.filter(user=user,
                                            goods_id=goods_id).first()

            if cart:
                cart.c_num += 1
                data['c_num'] = cart.c_num
                cart.save()
                return JsonResponse(data)

            else:
                cart = CartModel.objects.create(user=user,
                                                goods_id=goods_id)
                cart.c_num = 1
                data['c_num'] = cart.c_num
                cart.save()
                return JsonResponse(data)
        data['code'] = 1001
        data['msg'] = '用户未登录'
        return JsonResponse(data)


def sub_to_cart(request):
    if request.method == 'POST':
        user = request.user
        goods_id = request.POST.get('goods_id')

        data = {
            'code': 200,
            'msg': '请求成功',
        }

        if user.id:
            cart = CartModel.objects.filter(user=user,
                                            goods_id=goods_id).first()
            if cart:
                if cart.c_num == 1:
                    cart.delete()
                    data['c_num'] = 0
                    return JsonResponse(data)
                else:
                    cart.c_num -= 1
                    cart.save()
                    data['c_num'] = cart.c_num
                    return JsonResponse(data)

            data['code'] = 1002
            data['msg'] = '添加商品'
            return JsonResponse(data)
        data['code'] = 1001
        data['msg'] = '账户未登录'
        return JsonResponse(data)


def goods_num(request):
    if request.method == 'GET':
        user = request.user
        cart_list = []
        if user.id:
            carts = CartModel.objects.filter(user=user)
            for cart in carts:
                data = {
                    'user_id': cart.user.id,
                    'goods_id': cart.goods_id,
                    'c_num': cart.c_num,
                }
                cart_list.append(data)
            return JsonResponse({'carts': cart_list, 'code': 200})
        else:
            return JsonResponse({'carts': '', 'code': 1001})


def cart(request):
    if request.method == 'GET':
        user = request.user
        carts = CartModel.objects.filter(user=user)

        return render(request, 'cart/cart.html', {'carts': carts})


def change_cart_status(request):
    if request.method == 'POST':
        cart_id = request.POST.get('cart_id')
        cart = CartModel.objects.filter(id=cart_id).first()
        if cart.is_select:
            cart.is_select = False
        else:
            cart.is_select = True
        cart.save()

        return JsonResponse({'cart_status': cart.is_select, 'code': 200})


def goods_count(request):
    if request.method == 'GET':
        user = request.user

        carts = CartModel.objects.filter(user=user,
                                         is_select=True)
        count_prices = 0
        for cart in carts:
            count_prices += cart.goods.price * cart.c_num

        count_prices = round(count_prices, 3)
        return JsonResponse({'count': count_prices, 'code': 200})


# 订单
def make_order(request):
    if request.method == 'POST':
        user = request.user
        data = {
            'code': 200,
            'msg': '请求成功',
        }
        if user.id:
            o_num = get_order_num()
            order = OrderModel.objects.create(user=user,
                                              o_num=o_num,
                                              o_status=0)
            # cart 表示的就是购物车里的商品
            carts = CartModel.objects.filter(user=user,
                                             is_select=True)
            # 遍历购物车 让所有商品和订单建立关系
            for cart in carts:
                OrderGoodsModel.objects.create(goods_num=cart.c_num,
                                               goods=cart.goods,
                                               order=order)

            carts.delete()
            data['order_id'] = order.id

            return JsonResponse(data)
        data['code'] = 1001
        data['msg'] = '用户未登录'
        return JsonResponse(data)


def get_order(request):
    if request.method == 'GET':
        order_id = request.GET.get('order_id')
        order_goods = OrderGoodsModel.objects.filter(order_id=order_id)

        return render(request, 'order/order_info.html', {'order_goods': order_goods})


def change_order_status(request):
    if request.method == 'POST':
        data = {
            'code': 200,
            'msg': '请求成功',
        }
        user = request.user
        order_id = request.POST.get('order_id')

        order = OrderModel.objects.filter(user=user,
                                          id=order_id,
                                          o_status=0).first()
        order.o_status = 1
        order.save()
        data['o_status'] = order.o_status
        return JsonResponse(data)


def payed(request):
    if request.method == 'GET':
        user = request.user
        if user.id:
            # 代收货
            orders = OrderModel.objects.filter(o_status=1,
                                               user=user)

            return render(request, 'order/order_list_payed.html', {'orders': orders})


def wait_pay(request):
    if request.method == 'GET':
        user = request.user
        if user.id:
            orders = OrderModel.objects.filter(o_status=1,
                                               user=user)
            return render(request, 'order/order_list_wait_pay.html', {'orders': orders})
