from django.conf.urls import url

from users import views


urlpatterns = [
    url(r'mine/',views.mine,name='mine'),
    url(r'register/', views.register,name='register'),
    url(r'login/',views.login,name='login'),
    url(r'logout/',views.logout,name='logout'),


]