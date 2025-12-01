from django.urls import path
from .views_layanan import (
    LayananListView, LayananDetailView,
    LayananCreateView, LayananUpdateView,
    LayananDeleteView
)

urlpatterns = [
    path('', LayananListView.as_view(), name='layanan_list'),
    path('<int:pk>/', LayananDetailView.as_view(), name='layanan_detail'),
    path('create/', LayananCreateView.as_view(), name='layanan_create'),
    path('<int:pk>/edit/', LayananUpdateView.as_view(), name='layanan_edit'),
    path('<int:pk>/delete/', LayananDeleteView.as_view(), name='layanan_delete'),
]
