from django.views import generic
from hitcount.views import HitCountDetailView

from .models import Advertisement


class AdvertisementListView(generic.ListView):
    model = Advertisement


class AdvertisementDetailView(HitCountDetailView):
    model = Advertisement
    count_hit = True
