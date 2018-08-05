from django.conf.urls import url

from carts import views

urlpatterns = [
    # 更多商品
    url(r'list/', views.list, name='list'),
    # 购物车
    url(r'cart/', views.cart, name='cart'),
    # 商品详情
    url(r'detail/', views.detail, name='detail')
]
