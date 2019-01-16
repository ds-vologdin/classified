from django.urls import path

from . import views

urlpatterns = [
    path('', views.AdvertisementListView.as_view(), name='list_advertisements'),
    path('detail/<int:pk>', views.AdvertisementDetailView.as_view(),
         name='detail_advertisement')
]
