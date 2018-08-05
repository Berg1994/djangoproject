"""ttsx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from goods import views

app_name = 'user'
urlpatterns = [
    # 首页
    url('^$', views.index, name='index'),
    # 自带后台管理
    url('admin/', admin.site.urls),
    # 用户
    url('user/', include('user.urls', namespace='user'), ),
    # 购物车
    url('carts/', include('carts.urls', namespace='carts')),
    # 商品
    url('goods/', include('goods.urls', namespace='goods')),
    # 订单
    url('orders/', include('orders.urls', namespace='orders')),
]
