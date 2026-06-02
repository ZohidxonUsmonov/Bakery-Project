from django.contrib import admin

from .models import Service, Category,Product

# Register your models here.

admin.site.register(Service)
admin.site.register(Category)
admin.site.register(Product)