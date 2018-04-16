from django.conf.urls import url
from app01 import views

urlpatterns = [

    url(r'^index$', views.index),

    url(r'^show_static$', views.show_static),

    # http://127.0.0.1/add_user
    url(r'^add_user$', views.add_user),
    # http://127.0.0.1/do_add_user  ## 执行添加用户的逻辑
    url(r'^do_add_user$', views.do_add_user),
    # http://127.0.0.1/show_images  ## 显示头像页面
    url(r'^show_images', views.show_images),

    # http://127.0.0.1/show_page  ## 分页显示
    url(r'^show_page/(\d+)$', views.show_page),

    # http://127.0.0.1/select_area  ## 分页显示
    url(r'^select_area$', views.select_area),
    # http://127.0.0.1/select_child/num  ## 分页显示
    url(r'^select_child/(\d+)', views.select_child),

]