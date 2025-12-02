from django.urls import path
from .views_catatan import (
    CatatanListView, CatatanDetailView,
    CatatanCreateView, CatatanUpdateView,
    CatatanDeleteView
)

urlpatterns = [
    path('', CatatanListView.as_view(), name='catatan_list'),
    path('<int:pk>/', CatatanDetailView.as_view(), name='catatan_detail'),
    path('create/', CatatanCreateView.as_view(), name='catatan_create'),
    path('<int:pk>/edit/', CatatanUpdateView.as_view(), name='catatan_edit'),
    path('<int:pk>/delete/', CatatanDeleteView.as_view(), name='catatan_delete'),
]
