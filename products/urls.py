from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductList.as_view(), name=views.ProductList.name),
    path('<int:pk>/', views.ProductDetail.as_view(), name=views.ProductDetail.name),
]
