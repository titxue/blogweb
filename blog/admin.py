from django.contrib import admin

# Register your models here.
from blog.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish_date']


admin.site.register(Article, ArticleAdmin)
