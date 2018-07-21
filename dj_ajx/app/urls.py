from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^market/$', views.market, name='market'),
    url(r'^marketparams/(?P<typeid>\d+)/(?P<sort_id>\d+)/(?P<child_id>\d+)/', views.marketparams, name='marketparams'),
    url(r'^addtocart/', views.add_to_cart, name='add_to_cart'),
    url(r'^subtocart/', views.sub_to_cart, name='sub_to_cart'),
    #
    url(r'goodsnum/', views.goods_num, name='goods_num'),
    #
    url(r'cart/', views.cart, name='cart'),

    url(r'changecartstatus/', views.change_cart_status, name='change_cart_status'),

    url(r'goodscount/', views.goods_count, name='goods_count'),

    # 下单
    url(r'makeorder/', views.make_order, name='makeorder'),

    #待付款
    url(r'payed/',views.payed,name='payed'),
    #待支付
    url(r'waitpay',views.wait_pay,name='waitpay'),

    #订单页面
    url(r'getorder/',views.get_order, name='get_order'),
    url(r'changeorderstatus/',views.change_order_status,name='change_order_status'),
]
