from django.contrib import admin

from products.models import Products

@admin.register(Products)  
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','quantity')
    fields = ('name', 'description', 'image', ('price','quantity'))
    search_fields = ('name',)
    ordering = ('name',)
    