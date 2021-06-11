from django.contrib import admin
from .models import Items, Creator, Category

# Register your models here.

admin.site.register(Items)
admin.site.register(Creator)
admin.site.register(Category)
