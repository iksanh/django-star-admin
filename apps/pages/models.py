from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

# class Product(models.Model):
    
#     id    = models.AutoField(primary_key=True)
#     name  = models.CharField(max_length = 100) 
#     info  = models.CharField(max_length = 100, default = '')
#     price = models.IntegerField(blank=True, null=True)

#     def __str__(self):
#         return self.name


# ----------------------------------------------------------------------
# MASTER DATA
# ----------------------------------------------------------------------

class Layanan(models.Model):
    """
    HM / HGB / HGU
    """
    nama = models.CharField(max_length=100, default='')
    deskripsi = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.nama


class BerkasItem(models.Model):
    """
    Daftar berkas yang harus diperiksa (template)
    Contoh:
    - PBT
    - Peta Analisis
    - Surat Pernyataan Penguasaan Fisik
    """
    nama = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.nama}"


# ----------------------------------------------------------------------
# PEMOHON 
# ----------------------------------------------------------------------

class Permohonan(models.Model):
    """
    Data pemohon per permohonan layanan.
    """
    nama_pemohon = models.CharField(max_length=255)
    nik = models.CharField(max_length=50, null=True, blank=True)
    alamat = models.TextField(null=True, blank=True)

    layanan = models.ForeignKey(Layanan, on_delete=models.CASCADE)
    tanggal_permohonan = models.DateField()

    def __str__(self):
        return f"{self.nama_pemohon} - {self.layanan.nama}"

class CatatanTemplate(models.Model):
    """
    Catatan global yang dapat dipilih untuk setiap berkas.
    Contoh: OK, Belum Ada, Lengkapi luas, Coret & paraf batas, dll.
    """
    # berkas = models.ForeignKey(BerkasItem, on_delete=models.CASCADE, related_name="templates")
    berkas = models.ManyToManyField(BerkasItem, related_name="templates")
    teks = models.CharField(max_length=255)
    is_global = models.BooleanField(default=True)

    def __str__(self):
        return self.teks


class Pemeriksaan(models.Model):
    """
    Pemeriksaan berkas per pemohon.
    """
    pemohon = models.ForeignKey(Permohonan, on_delete=models.CASCADE)
    berkas = models.ForeignKey(BerkasItem, on_delete=models.CASCADE)

    # Beberapa catatan standar (multiple select)
    catatan = models.ManyToManyField(CatatanTemplate, blank=True)

    # Catatan khusus (tidak global)
    catatan_baru = models.TextField(blank=True, null=True)

    tanggal_koreksi = models.DateField(auto_now=True)

    def __str__(self):
        return f"Pemeriksaan {self.pemohon.nama_pemohon} - {self.berkas.nama}"