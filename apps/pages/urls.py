from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('permohonan/', views.permohonan, name='permohonan'),
    path("pemohon/<int:pemohon_id>/print/",views.print_detail_pemohon, name="print_detail_pemohon"),
    
    path('pemeriksaan/input/<int:pemohon_id>/', views.pemeriksaan_input, name='pemeriksaan_input'),
    # AJAX endpoint untuk membuat CatatanTemplate global
    path('ajax/create-catatan/', views.ajax_create_catatan, name='ajax_create_catatan'),
     path('pemeriksaan/detail/<int:pemohon_id>/', 
         views.detail_pemohon, 
         name='detail_pemohon'),

    path('layanan/', include('apps.pages.urls_layanan')),
    path('berkas/', include('apps.pages.urls_berkas_item')),
  
]
