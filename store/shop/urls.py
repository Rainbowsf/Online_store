from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.CategoryListView.as_view(), name='category-list'),
    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),
    path('make_an_order/', views.make_order, name='make_order'),
    path('delivery/', views.delivery, name='delivery'),
    path('<slug:slug>/', views.CategoryDetailView.as_view(), name='product-list'),
    path('products/<slug:slug>/', views.ProductDetailView.as_view(), name='product-detail'),

]
