from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inpr/',views.in_product, name='in_product'),
    path('createform/',views.createform, name='createform'),
    path('outpr/',views.out_product, name='out_product'),
    path('out_createform/',views.out_create_form, name='out_createform'),
    path('date/',views.date,name='date'),
    path('test/',views.test,name='test')
]