from django.conf.urls import url

from goods import views

urlpatterns = [
    url(r'creategoods/', views.create_goods, name='create_goods'),
    url(r'detail/(\d+)/', views.good_detail, name='good_detail'),
    url(r'^addcount/',views.add_count,name='add_count'),
    url(r'^subcount/',views.sub_count,name='sub_count'),
    url(r'^count/',views.show_count,name='show_count'),

]
