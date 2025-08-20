from django.contrib import admin

from blog.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'photo', 'created_at', 'publication_at', 'quantity_count',)
    list_editable = ('name', 'description', 'photo', 'publication_at', 'quantity_count',)
