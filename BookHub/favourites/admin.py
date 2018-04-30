from django.contrib import admin

from favourites.models import Favourite


class FavouriteInline(admin.TabularInline):
    model = Favourite


class FavouriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'added_at',)
    search_fields = ('user', 'book',)


admin.site.register(Favourite, FavouriteAdmin)
