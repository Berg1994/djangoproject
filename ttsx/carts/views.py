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


def add_cart_count(request):
    if request.method == 'POST':
        data = {
            'code': 200,
            'msg': '请求成功'
        }
        goods_id = request.GET.get('goods_id')
        user = request.user
        if user.id:
            cart = CartModel.objects.filter(user_id=user.id).first()
            if cart:
                cart_goods = CartGoodsMOdel.objects.filter(cart_id=cart.id, goods_id=goods_id).first()
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


def sub_cart_count(request):
    if request.method == 'POST':
        pass


# 商品详情
def detail(request):
    if request.method == 'GET':
        return render(request, 'back_manage/detail.html')
