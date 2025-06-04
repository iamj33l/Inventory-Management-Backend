from django.urls import path

from . import views

urlpatterns = [
    path('', views.product_movement_list, name='product-movement-list'),
    path('<int:pk>/', views.product_movement_detail, name='product-movement-detail'),
    path('create/', views.product_movement_create, name='product-movement-create'),
    path('<int:pk>/update/', views.product_movement_update, name='product-movement-update'),
    path('<int:pk>/delete/', views.product_movement_delete, name='product-movement-delete'),
]
