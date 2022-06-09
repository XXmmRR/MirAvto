from django.contrib import admin
from .models import PartList, Category, Product, Mark, Order, Type

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
    raw_id_fields = ['part_list']


@admin.register(Product)
class PartAdmin(admin.ModelAdmin):
    list_display = ('category', 'article', 'article_second', 'name', 'price', 'image_tag', 'type')
    search_fields = ('category', 'article', 'article_second', 'name', 'price', 'type')
    ordering = ('name', 'price')
    prepopulated_fields = {'part_slug': ('name',)}
    raw_id_fields = ['category', 'type']


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'slug')
    search_fields = ('category', 'name')
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ['category']


admin.site.register(Order)
