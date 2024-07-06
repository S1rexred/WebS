from django.contrib import admin

from product.models import Product, Phone

admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','quantity')
    fields = ('name', 'description', 'image', ('price','quantity'))
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(Phone)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','phone','message')
    fields = ('name', 'message', 'phone')
    search_fields = ('name',)
    ordering = ('name',)