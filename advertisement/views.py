from django.views import generic
from hitcount.views import HitCountDetailView

from .models import Advertisement


class AdvertisementListView(generic.ListView):
    model = Advertisement

    def get_queryset(self):
        # Скорее всего будет актуально, такие поля как 'city' лучше джойнить...
        return Advertisement.objects.select_related('city', 'customer').all()


class AdvertisementDetailView(HitCountDetailView):
    model = Advertisement
    count_hit = True
