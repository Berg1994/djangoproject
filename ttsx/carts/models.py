from django.db import models

from goods.models import GoodsModel
from user.models import UserModel


# 购物车
class CartModel(models.Model):
    # 用户外键
    user = models.ForeignKey(UserModel)
    c_g = models.ManyToManyField(GoodsModel)

    class Meta():
        db_table = 'ttsx_cart'


# 中间键
class CartGoodsMOdel(models.Model):
    # 用户外键
    cart = models.ForeignKey(CartModel)
    # 商品外键
    goods = models.ForeignKey(GoodsModel)
    # 购买数量
    count = models.IntegerField(default=1)

    class Meta():
        db_table = 'ttsx_cart_goods'
