from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.views.generic import ListView, DetailView
from urllib import request, response
from django.views.generic.edit import FormMixin
from cart.forms import CartAddProductForm


class CategoryListView(ListView):
    """
        Представление списка категорий
    """
    model = Category
    template_name = 'base.html'
    context_object_name = 'category_list'


class CategoryDetailView(DetailView):
    """
        Представление списка товаров одной категории
    """
    model = Category
    template_name = 'shop/product-list.html'
    context_object_name = 'category'

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(*args, **kwargs)
        context['product_list'] = Product.objects.filter(available=True, category=self.object)
        return context


class ProductDetailView(DetailView, FormMixin):
    """
        Представление товара
    """
    model = Product
    template_name = 'shop/product-detail.html'
    context_object_name = 'product_detail'
    form_class = CartAddProductForm

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        return context