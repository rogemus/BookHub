from django.contrib import admin

from favourites.models import Favourite


class FavouriteInline(admin.TabularInline):
    model = Favourite


class FavouriteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Favourite, FavouriteAdmin)
