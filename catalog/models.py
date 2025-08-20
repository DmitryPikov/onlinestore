from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(max_length=500, verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(max_length=500, verbose_name='Описание')
    photo = models.ImageField(upload_to='photo/products/', verbose_name='Изображение', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата последнего изменения')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name
