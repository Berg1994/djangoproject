import random

from django.http import JsonResponse
from django.shortcuts import render

from carts.models import CartGoodsMOdel, CartModel
from goods.models import GoodsModel, TypeModel


def create_goods(request):
    if request.method == 'GET':
        for _ in range(3):
            g_name = '3'
            g_img = 'back_static\images\goods\goods004.jpg'
            g_kucun = '1000'
            g_unit = '500g'
            g_price = 5.5
            is_delete = False
            g_type = TypeModel.objects.filter(id=2).first()
            GoodsModel.objects.create(g_name=g_name, g_type=g_type, g_price=g_price, g_unit=g_unit, g_kucun=g_kucun,
                                      g_img=g_img, is_delete=is_delete, )
    return '创建成功'


# 首页
def index(request):
    if request.method == 'GET':

        typeinfos = TypeModel.objects.all()
        type_dict = {}
        type_list = []
        for typeinfo in typeinfos:
            goods = typeinfo.goodsmodel_set.all()[0:4]
            type_dict[typeinfo.t_name] = goods
            type_list.append(typeinfo)

        return render(request, 'back_manage/index.html', {'type_dict': type_dict, 'type_list': type_list})


# 商品详情
def good_detail(request, id):
    if request.method == 'GET':
        goods = GoodsModel.objects.filter(id=id).first()
        return render(request, 'back_manage/detail.html', {'goods': goods})


# 添加商品
def add_count(request):
    if request.method == 'POST':
        user = request.user
        goods_id = request.POST.get('goods_id')

        data = {
            'code': 200,
            'msg': '请求成功',
        }

        if user.id:
            cart = CartModel.objects.filter(user_id=user.id).first()

            if cart:

                cart_goods = CartGoodsMOdel.objects.filter(cart_id=cart.id, goods_id=goods_id).first()
                if cart_goods:

                    cart_goods.count += 1
                    data['count'] = cart_goods.count
                    cart_goods.save()
                    return JsonResponse(data)
                else:
                    cart_goods = CartGoodsMOdel.objects.create(cart_id=cart.id, goods_id=goods_id)
                    cart_goods.count = 1
                    data['count'] = 1
                    return JsonResponse(data)
            else:
                cart = CartModel.objects.create(user_id=user.id)
                cart_goods = CartGoodsMOdel.objects.create(cart_id=cart.id, goods_id=goods_id)
                cart_goods.count = 1
                return JsonResponse(data)
        data['code'] = 1001
        data['msg'] = '用户未登录'
        return JsonResponse(data)


# 删除商品
def sub_count(request):
    if request.method == 'POST':
        user = request.user
        goods_id = request.POST.get('goods_id')

        data = {
            'code': 200,
            'msg': '请求成功',
        }

        if user.id:
            cart = CartModel.objects.filter(user_id=user.id).first()
            if cart:
                cart_goods = CartGoodsMOdel.objects.filter(cart_id=cart.id, goods_id=goods_id).first()
                if cart_goods:
                    if cart_goods.count == 1:
                        cart_goods.delete()
                        data['count'] = 0

                        return JsonResponse(data)
                    else:
                        cart_goods.count -= 1
                        data['count'] = cart_goods.count
                        cart_goods.save()
                        return JsonResponse(data)
                else:
                    data = {
                        'code': 1002,
                        'msg': '没有商品可以删除'
                    }

                    return JsonResponse(data)
            else:
                data = {
                    'code': 1003,
                    'msg': '没有购物车'
                }

                return JsonResponse(data)
        data['code'] = 1001
        data['msg'] = '用户未登录'
        return JsonResponse(data)


def show_count(request):
    if request.method == 'GET':
        user = request.user

