from django.urls import path

from . import views

urlpatterns = [
    path('', views.location_list, name='location-list'),
    path('<int:pk>/', views.location_detail, name='location-detail'),
    path('create/', views.location_create, name='location-create'),
    path('<int:pk>/update/', views.location_update, name='location-update'),
    path('<int:pk>/delete/', views.location_delete, name='location-delete'),
]
