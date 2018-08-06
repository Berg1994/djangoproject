from django.conf.urls import url

from goods import views

urlpatterns = [
    #创建商品
    url(r'^creategoods/', views.create_goods, name='create_goods'),
    #商品详情
    url(r'^goods_detail/', views.goods_detail, name='goods_detail'),
    #添加
    url(r'^addcount/',views.add_count,name='add_count'),
    #删减商品
    url(r'^subcount/',views.sub_count,name='sub_count'),
    #返回商品数量
    url(r'^count/',views.show_count,name='show_count'),
    #添加到购物车
    url(r'^addtocart/',views.add_to_cart,name='add_to_cart'),


]
