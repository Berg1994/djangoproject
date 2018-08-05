from django.db import models

# 订单表模型
from goods.models import GoodsModel
from user.models import UserModel


class OrderModel(models.Model):
    #订单ID
    o_id = models.IntegerField( primary_key=True)
    user = models.ForeignKey(UserModel)
    #订单创建时间
    o_create_time = models.DateTimeField(auto_now_add=True)
    #是否支付
    o_is_payed = models.BooleanField(default=False)
    #订单总价
    o_total = models.FloatField(max_length=10, default=2)
    #收货地址
    o_address = models.CharField(max_length=100)

    class Meta():
        db_table = 'ttsx_order'


# 订单详情表
class OrderGoodModel(models.Model):

    goods = models.ForeignKey(GoodsModel)
    orders = models.ForeignKey(OrderModel)
    #商品数量
    goods_num = models.IntegerField(default=1)
    #商品价格
    price = models.FloatField(default=1)
    #是否统计到销量内
    is_counted = models.BooleanField(default=False)


class sales(models.Model):
    # 水果名称
    goods = models.ForeignKey(GoodsModel)
    # 销量
    count = models.IntegerField(default=0)
    # 销售额
    totalprice = models.FloatField(default=0)

    class Meta():
        db_table = 'ttsx_sales'
