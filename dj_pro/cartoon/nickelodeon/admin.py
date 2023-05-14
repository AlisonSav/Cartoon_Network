
from django.contrib import admin

from .models import Cartoon, CartoonUser


class CartoonUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'surname')


class CartoonAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year', 'rating')


admin.site.register(Cartoon, CartoonAdmin)
admin.site.register(CartoonUser, CartoonUserAdmin)

