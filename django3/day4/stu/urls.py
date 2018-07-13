# 在app应用下的urls
from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from stu import views
#生成一个路由
router = SimpleRouter()
#处理这个视图类
router.register('^student',views.StudentSource)

urlpatterns = [

    url(r'^s_index/',views.s_index,name='s_index'),
]

urlpatterns += router.urls