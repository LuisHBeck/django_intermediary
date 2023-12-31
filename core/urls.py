from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('product/', views.product, name='product'),
    path('product/<int:pk>/', views.product_img, name='product_img')
]