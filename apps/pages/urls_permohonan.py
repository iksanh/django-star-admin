from django.urls import path
from .views_permohonan import (
    PermohonanListView, PermohonanDetailView,
    PermohonanCreateView, PermohonanUpdateView,
    PermohonanDeleteView
)

urlpatterns = [
    path('', PermohonanListView.as_view(), name='permohonan'),
    path('<int:pk>/', PermohonanDetailView.as_view(), name='permohonan_detail'),
    path('create/', PermohonanCreateView.as_view(), name='permohonan_create'),
    path('<int:pk>/edit/', PermohonanUpdateView.as_view(), name='permohonan_edit'),
    path('<int:pk>/delete/', PermohonanDeleteView.as_view(), name='permohonan_delete'),
]
