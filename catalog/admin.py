from django.contrib import admin
from .models import PartList, Category, Part, Mark

# Register your models here.


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(PartList)
class PartListAdmin(admin.ModelAdmin):
    list_display = ('list_name', 'mark',)
    search_fields = ('list_name', 'mark',)
    ordering = ('list_name',)
    prepopulated_fields = {'list_slug': ('list_name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('part_list', 'category_name')
    search_fields = ('part_list', 'category_name')
    ordering = ('part_list',)
    prepopulated_fields = {'category_slug': ('category_name',)}


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ('category', 'article', 'article_second', 'part_name', 'part_price')
    search_fields = ('category', 'article', 'article_second', 'part_name', 'part_price')
    ordering = ('part_name', 'part_price')
    prepopulated_fields = {'part_slug': ('part_name',)}