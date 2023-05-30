from django.contrib import admin
from . import models

# admin.site.register(models.Color, ColorAdmin)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'slug', 'status', "position", "parent")
    list_filter = ('status',)
    search_fields = ('category_name', "slug")
    list_editable = ('status',)
    prepopulated_fields = {'slug': ('category_name',)}
