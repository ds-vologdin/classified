from django.contrib import admin

from .models import Advertisement
from .models import City


class AdvertisementInline(admin.TabularInline):
    model = Advertisement


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_publication', 'city', 'customer', 'ad_hit_count')

    def ad_hit_count(self, ad):
        return ad.hit_count.hits


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [AdvertisementInline]
