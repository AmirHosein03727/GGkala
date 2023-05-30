from django.contrib import admin
from .models import SexToys
from . import models


@admin.register(models.Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('color_name', 'color_rgb', 'slug', 'status', "position")
    list_filter = ('status',)
    search_fields = ('color_name', 'color_rgb', "slug")
    list_editable = ('status',)
    prepopulated_fields = {'slug': ('color_name',)}


@admin.register(SexToys)
class SexToysAdmin(admin.ModelAdmin):
    list_display = ('title_short', 'return_pic', 'slug', 'brand', 'inventory', "publish", 'publisher', 'created_short', "show_category")
    list_filter = ('inventory', 'brand')
    search_fields = ('title', 'about')
    list_editable = ('inventory', 'publish')
    prepopulated_fields = {'slug': ('title',)}
    actions = ["make_published", "un_published"]

    # def show_category(self, obj):
    #     return ", ".join([cat.category_name for cat in obj.category.return_truestatus()])

    @admin.action(description="Mark selected stories as published")
    def make_published(self, request, queryset):
        queryset.update(publish="published")

    @admin.action(description="Mark selected stories as unpublished")
    def un_published(self, request, queryset):
        queryset.update(publish="unpublished")

