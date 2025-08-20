from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=50, verbose_name='Заголовок')
    description = models.TextField(max_length=500, verbose_name='Содержимое')
    photo = models.ImageField(upload_to='photo/blogs/', verbose_name='Изображение', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    publication_at = models.BooleanField(verbose_name='Признак публикации')
    quantity_count = models.PositiveIntegerField(verbose_name='Количество просмотров', default=0)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.name
