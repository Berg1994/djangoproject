from json import loads

from django.core import serializers

from django.http import JsonResponse
from django.shortcuts import render

# 更多列表
from carts.models import CartModel, CartGoodsMOdel


def list(request):
    if request.method == 'GET':
        return render(request, 'back_manage/list.html')


# 购物车
def cart(request):
    if request.method == 'GET':
        goods_list = []
        goods_dict = {}
        user = request.user
        if user.id:
            cart = CartModel.objects.filter(user_id=user.id).first()
            if cart:
                cart_goods_list = cart.cartgoodsmodel_set.filter(in_cart=1).all()
                cart_goods_count = cart.cartgoodsmodel_set.filter(in_cart=1).count()
                for goods in cart_goods_list:
                    goods_dict[goods.goods.g_name] = goods
                goods_list.append(goods_dict)

                return render(request, 'back_manage/cart.html',
                              {'goods_list': goods_list, 'cart_goods_count': cart_goods_count})
            return render(request, 'back_manage/cart.html', {'goods_list': ''})
        return render(request, 'back_manage/cart.html', {'goods_list': ''})


# 增添商品
def add_cart_count(request):
    if request.method == 'POST':
        data = {
            'code': 200,
            'msg': '请求成功'
        }
        goods_id = request.POST.get('goods_id')
        user = request.user
        if user.id:
            cart = CartModel.objects.filter(user_id=user.id).first()
            if cart:
                cart_goods = CartGoodsMOdel.objects.filter(cart_id=cart.id, goods_id=goods_id, in_cart=1).first()
                if cart_goods:
                    cart_goods.count += 1
                    cart_goods.save()
                    data['count'] = cart_goods.count
                    return JsonResponse(data)
                cart_goods = CartGoodsMOdel.objects.create(cart_id=cart.id, goods_id=goods_id, count=1)
                data['count'] = 1
                return JsonResponse(data)
        data['code'] = '1005'
        data['msg'] = '请添加商品'
        return JsonResponse(data)


# 删减商品
def sub_cart_count(request):
    if request.method == 'POST':
        data = {
            'code': 200,
            'msg': '请求成功'
        }
        goods_id = request.POST.get('goods_id')
        user = request.user
        if user.id:
            cart = CartModel.objects.filter(user_id=user.id).first()
            if cart:
                cart_goods = CartGoodsMOdel.objects.filter(cart_id=cart.id, goods_id=goods_id, in_cart=1).first()
                if cart_goods:
                    if cart_goods.count == 1:
                        data['count'] = 0
                        cart_goods.delete()
                        return JsonResponse(data)
                    cart_goods.count -= 1
                    data['count'] = cart_goods.count
                    cart_goods.save()
                    return JsonResponse(data)
                data['code'] = 1006
                data['msg'] = '请添加商品'
                return JsonResponse(data)


# 展示购物车商品数量
def cart_count(request):
    if request.method == 'GET':

        user = request.user
        if user.id:
            cart = CartModel.objects.filter(user_id=user.id).first()
            if cart:
                cart_goods_list = CartGoodsMOdel.objects.filter(cart=cart.id,
                                                                in_cart=1).all()
                goods_list = []
                for goods in cart_goods_list:
                    data = {
                        'price': '%.2f' % (goods.goods.g_price),
                        'count': goods.count,
                        'id': goods.goods_id,
                        'total': '%.2f' % (goods.goods.g_price * goods.count)
                    }
                    goods_list.append(data)

                return JsonResponse({'goods_list': goods_list, 'code': 200})


# 商品详情
def detail(request):
    if request.method == 'GET':
        return render(request, 'back_manage/detail.html')


# 删除商品
def del_cart_goods(request):
    if request.method == 'POST':
        data = {
            'code': 200,
            'msg': '请求成功'
        }
        user = request.user
        goods_id = request.POST.get('goods_id')

        if user.id:
            cart = CartModel.objects.get(user_id=user.id)
            if cart:
                cart_goods = CartGoodsMOdel.objects.filter(cart=cart.id,
                                                           goods_id=goods_id,
                                                           in_cart=1,
                                                           )
                cart_goods.delete()
                return JsonResponse(data)
            data['msg'] = '请添加商品'
            data['code'] = 1006
            return JsonResponse(data)
        data['msg'] = '请用户登录'
        data['code'] = 1001
        return JsonResponse(data)
