from django.contrib import admin

from .models import Cartoon, CartoonUser


@admin.register(CartoonUser)
class CartoonUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'surname', 'email')


class CartoonAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year', 'country', 'rating', 'rating_status')
    list_editable = ('year', 'rating', 'country')
    ordering = ('title', 'year', 'rating')
    list_per_page = 10
    search_fields = ['title']

    @admin.display(ordering='rating', description='Status')
    def rating_status(self, cartoon: Cartoon):
        if cartoon.rating < 50:
            return "I don't want to watch it"
        elif cartoon.rating < 85:
            return "Mmm... maybee..."
        else:
            return "Good!"


admin.site.register(Cartoon, CartoonAdmin)
# admin.site.register(CartoonUser, CartoonUserAdmin)
