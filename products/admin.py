from django.contrib import admin

from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'price','sale_price']
    search_fields = ['title','description']
    list_filter = ['price']
    list_editable = ['sale_price']

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
