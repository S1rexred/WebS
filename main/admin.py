from django.contrib import admin

from main.models import Menu, Products

#admin.site.register(Menu)
#admin.site.register(Products)

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}