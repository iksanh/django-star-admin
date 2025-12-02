from django.urls import path, include

from . import views
from .views_permohonan import PermohonanCreateView

urlpatterns = [
    path('', views.index, name='index'),
    # path('permohonan/', views.permohonan, name='permohonan'),
    
    # path('permohonan/create', PermohonanCreateView.as_view(), name='permohonan_create'),
    path("pemohon/<int:pemohon_id>/print/",views.print_detail_pemohon, name="print_detail_pemohon"),
    
    path('pemeriksaan/input/<int:pemohon_id>/', views.pemeriksaan_input, name='pemeriksaan_input'),
    # AJAX endpoint untuk membuat CatatanTemplate global
    path('ajax/create-catatan/', views.ajax_create_catatan, name='ajax_create_catatan'),
    path('ajax/get-kecamatan/<str:district_id>/', views.get_villages, name='ajax_get_kecamatan'),
     path('pemeriksaan/detail/<int:pemohon_id>/', 
         views.detail_pemohon, 
         name='detail_pemohon'),

    path('layanan/', include('apps.pages.urls_layanan')),
    path('catatan/', include('apps.pages.urls_catatan')),
    path('berkas/', include('apps.pages.urls_berkas_item')),
    path('permohonan/', include('apps.pages.urls_permohonan')),
  
]
