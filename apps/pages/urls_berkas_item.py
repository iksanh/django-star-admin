from django.urls import path
from .views_berkas_item import (
    BerkasItemListView, BerkasItemDetailView,
    BerkasItemCreateView, BerkasItemUpdateView,
    BerkasItemDeleteView, pengaturan_urutan_berkas
)

urlpatterns = [
    path('', BerkasItemListView.as_view(), name='berkasitem_list'),
    path('<int:pk>/', BerkasItemDetailView.as_view(), name='berkasitem_detail'),
    path('create/', BerkasItemCreateView.as_view(), name='berkasitem_create'),
    path('<int:pk>/edit/', BerkasItemUpdateView.as_view(), name='berkasitem_edit'),
    path('<int:pk>/delete/', BerkasItemDeleteView.as_view(), name='berkasitem_delete'),
    path('<int:pk>/delete/', BerkasItemDeleteView.as_view(), name='berkasitem_delete'),
    path('urutan/', pengaturan_urutan_berkas, name='berkasitem_urutan'),
]
