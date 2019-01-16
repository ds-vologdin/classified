from django.contrib import admin

from .models import Advertisement
from .models import City


class AdvertisementInline(admin.StackedInline):
    model = Advertisement


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_publication', 'unique_views', 'city', 'customers')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [AdvertisementInline]
