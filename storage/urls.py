from django.contrib import admin
from django.urls import path
from . import views

app_name = 'storage'

urlpatterns = [
    path('', views.sklads_list, name='sklads_list'),  # Главная страница
    path('edinica_list/', views.edinica_list, name='edinica_list'),  # Страница со всем инвентарем
    path('sklads/<int:sklads_id>/', views.sklads_floors, name='sklads_floors'),  # Список этажей на складе
    path('etazh/<int:etazh_id>/', views.floor_cabinets, name='floor_cabinets'),  # Список кабинетов на этаже
    path('cabinets/<int:kabinet_id>/', views.cabinet_units, name='cabinet_units'),
    path('detail/<int:pk>/', views.edinica_detail, name='edinica_detail' ),
    path('create/', views.create_edinica, name='create_edinica'),
    path('edit/<int:edinica_id>/', views.edit_edinica, name='edit_edinica'),
    path('delete/<int:edinica_id>/', views.delete_edinica, name='delete_edinica'),  # Единицы техники в кабинете
    # Другие URL-маршруты
]