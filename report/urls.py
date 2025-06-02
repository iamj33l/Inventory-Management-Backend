from django.urls import path

from . import views

urlpatterns = [
    path('product-balance/', views.product_balance_list, name='product-balance-list'),
]