from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from carts import views

# 生成一个路由
router = SimpleRouter()
# 注册这个视图类
# router.register('^cart_count',views.Cart_count)


urlpatterns = [
    # 更多商品
    url(r'list/', views.list, name='list'),
    # 购物车
    url(r'cart/', views.cart, name='cart'),
    # 商品详情
    url(r'detail/', views.detail, name='detail'),
    # 添加商品数量
    url(r'^addcount/', views.add_cart_count, name='add_cart_count'),
    # 删减商品数量
    url(r'^subcount/', views.sub_cart_count, name='sub_cart_count'),
    # 展示购物车商品数量
    url(r'^count/', views.cart_count, name='cart_count'),
    # 删除购物车商品
    url(r'^delcartgoods/', views.del_cart_goods, name='del_cart_goods'),

]
urlpatterns += router.urls
