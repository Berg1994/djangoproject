from django.db import models


class UserModel(models.Model):
    # 用户名称
    username = models.CharField(max_length=12, null=False)
    # 密码
    pwd = models.CharField(max_length=200)
    # 邮箱
    email = models.CharField(max_length=30)
    # 收件人名称
    show = models.CharField(max_length=20, null=True)
    # 收件人地址
    address = models.CharField(max_length=50, null=True)
    # 收件人邮编
    youbian = models.CharField(max_length=50, null=True)
    # 收件人电话
    phone = models.CharField(max_length=11, null=True)

    class Meta:
        db_table = 'ttsx_user'


class UserTicket(models.Model):
    # 关联用户外键
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    ticket = models.CharField(max_length=256)
    out_time = models.DateTimeField()

    class Meta:
        db_table = 'ttsx_user_ticket'
