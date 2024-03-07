from django.contrib import admin

from myapp.models import User, Product, Purchase

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Purchase)