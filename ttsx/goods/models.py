from django.db import models


# 商品类型
class TypeModel(models.Model):
    #类型名称
    t_name = models.CharField(max_length=20)
    t_img = models.CharField(max_length=256,null=True)
    is_delete = models.BooleanField(default=False)

    class Meta():
        db_table = 'ttsx_type'


# 商品模型
class GoodsModel(models.Model):
    #商品名称
    g_name = models.CharField(max_length=20)
    #商品图片
    g_img = models.CharField(max_length=255)
    #商品价格
    g_price = models.FloatField(default=1)
    #是否选择？
    is_delete = models.BooleanField(default=False)
    #商品单位
    g_unit = models.CharField(default='500g', max_length=20)
    #商品库存
    g_kucun = models.CharField(max_length=10)
    #类型关联外键
    g_type = models.ForeignKey(TypeModel)
    #商品点击次数
    g_click = models.IntegerField(default=0)

    class Meta():
        db_table = 'ttsx_goods'

