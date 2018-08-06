from django.conf.urls import url

from carts import views

urlpatterns = [
    # 更多商品
    url(r'list/', views.list, name='list'),
    # 购物车
    url(r'cart/', views.cart, name='cart'),
    # 商品详情
    url(r'detail/', views.detail, name='detail'),
    #添加商品数量
    url(r'^add_cart_count/', views.add_cart_count,name='add_cart_count'),
    #删减商品数量
    url(r'sub_cart_count/',views.sub_cart_count,name='sub_cart_count'),

]
