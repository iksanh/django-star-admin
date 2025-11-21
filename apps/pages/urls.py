from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('permohonan/', views.permohonan, name='permohonan'),
    path('pemeriksaan/input/<int:pemohon_id>/', views.pemeriksaan_input, name='pemeriksaan_input'),
    # AJAX endpoint untuk membuat CatatanTemplate global
    path('ajax/create-catatan/', views.ajax_create_catatan, name='ajax_create_catatan'),
     path('pemeriksaan/detail/<int:pemohon_id>/', 
         views.detail_pemohon, 
         name='detail_pemohon'),
  
]
