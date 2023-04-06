from django.contrib import admin
from .models import Shoes
# Register your models here.


@admin.register(Shoes)
class ShoesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'price', 'date']