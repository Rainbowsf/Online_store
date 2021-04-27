# -*- coding: utf-8 -*-
from django.db import models


class Category(models.Model):
    """
       Модель категории
     """
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название категории")
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name="Слаг для ссылки")
    image = models.ImageField(upload_to='categories/%Y/%m/%d', blank=True, verbose_name="Изображение категории")

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    """
      Модель товара
    """
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name="Категория")
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название товара")
    slug = models.SlugField(max_length=200, db_index=True, verbose_name="Слаг для ссылки")
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name="Изображение товара")
    description = models.TextField(blank=True, verbose_name="Описание товара")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена товара")
    stock = models.PositiveIntegerField(verbose_name="Количество")
    available = models.BooleanField(default=True, verbose_name="Доступен для продажи")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

