from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #path('',views.list_products, name='list_products'),
    url(r'^$',views.list_products, name='list_products'),
    path('create/', views.create_products, name='create_products'),
    path('update/<int:id>/',views.update_products, name='update_products'),
    path('delete/<int:id>/', views.delete_products, name='delete_products'),
]
