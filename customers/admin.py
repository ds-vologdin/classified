from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Customer
from advertisement.models import Advertisement


class AdvertisementInline(admin.StackedInline):
    model = Advertisement


@admin.register(Customer)
class CustomerAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    inlines = [AdvertisementInline]
