from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Permohonan, CatatanTemplate
from .forms import PermohonanForm

# Register your models here.

@admin.register(Permohonan)
class PermohonanAdmin(admin.ModelAdmin):
    form = PermohonanForm
    list_display = (
        # "id",
        "nama_pemohon",
        "nik",
        "layanan",
        "tanggal_permohonan",
        "input_pemeriksaan_link"
    )
    list_filter = ("layanan",)
    search_fields = ("nama_pemohon", "nik", "alamat")
    ordering = ("-tanggal_permohonan",)
    list_per_page = 25

    def input_pemeriksaan_link(self, obj):
        url = reverse("pemeriksaan_input", args=[obj.id])
        return format_html('<a class="btn btn-sm btn-outline-gray-600 btn-primary" href="{}"> Periksa Berkas</a>', url)


@admin.register(CatatanTemplate)
class CatatanTemplateAdmin(admin.ModelAdmin):
    list_display = ("teks", "is_global")
    list_filter = ("is_global",)
    search_fields = ("teks",)
    filter_horizontal = ("berkas",)   # 🔥 bikin field ManyToMany jadi checklist/dual list