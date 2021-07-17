from django.contrib import admin
from . import models        #импорт models.py, чтобы ниже обратиться к моделям из него


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
