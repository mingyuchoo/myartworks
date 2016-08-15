from django.contrib import admin

from .models import Category, Field


class CategoryAdmin(admin.ModelAdmin):
    pass


class FieldAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Field, FieldAdmin)
