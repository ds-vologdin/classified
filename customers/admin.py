from django.contrib import admin

from .models import Customer
from advertisement.models import Advertisement


class AdvertisementInline(admin.StackedInline):
    model = Advertisement


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name')
    inlines = [AdvertisementInline]
