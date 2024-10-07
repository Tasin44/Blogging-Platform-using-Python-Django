from django.contrib import admin

# Register your models here.
# Here we are registering our table in the admin. 
from django.contrib import admin
from .models import Product

admin.site.register(Product)

