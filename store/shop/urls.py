from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CategoryListView.as_view(), name='category-list'),
    path('<slug:slug>/', views.CategoryDetailView.as_view(), name='product-list'),
    path('products/<slug:slug>/', views.ProductDetailView.as_view(), name='product-detail')
]