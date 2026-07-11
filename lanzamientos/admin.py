from django.contrib import admin
from .models import Categoria, Producto

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
