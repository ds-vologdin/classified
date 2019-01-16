from django.views import generic

from .models import Advertisement


class AdvertisementListView(generic.ListView):
    model = Advertisement


class AdvertisementDetailView(generic.DetailView):
    model = Advertisement

