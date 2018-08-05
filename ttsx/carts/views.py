from django.shortcuts import render





# 更多列表
def list(request):
    if request.method == 'GET':
        return render(request, 'back_manage/list.html')


# 购物车
def cart(request):
    if request.method == 'GET':
        return render(request, 'back_manage/cart.html')


# 商品详情
def detail(request):
    if request.method == 'GET':
        return render(request, 'back_manage/detail.html')
