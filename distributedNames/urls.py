from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.add, name='index'),
    url(r'^register/', views.name_list, name='nameRegister'),
    url(r'^list/', views.name_list, name='nameList'),
    url(r'^nodes/', views.node_list, name='nodeList'),
]