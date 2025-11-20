from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Product(models.Model):
    
    id    = models.AutoField(primary_key=True)
    name  = models.CharField(max_length = 100) 
    info  = models.CharField(max_length = 100, default = '')
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


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
    layanan = models.ForeignKey(Layanan, on_delete=models.CASCADE, related_name="berkas_items")

    wajib = models.BooleanField(default=True)  # apakah wajib?

    def __str__(self):
        return f"{self.nama} - {self.layanan.nama}"


# ----------------------------------------------------------------------
# PERMOHONAN
# ----------------------------------------------------------------------

class Permohonan(models.Model):
    """
    Data permohonan layanan (tanpa upload file).
    """
    nama_pemohon = models.CharField(max_length=255)
    nik = models.CharField(max_length=50, null=True, blank=True)
    layanan = models.ForeignKey(Layanan, on_delete=models.CASCADE)

    tanggal_permohonan = models.DateField(auto_now_add=True)

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('revisi', 'Revisi'),
        ('approved', 'Approved'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.nama_pemohon} - {self.layanan.nama}"


# ----------------------------------------------------------------------
# BERKAS PER PERMOHONAN
# ----------------------------------------------------------------------

class PermohonanBerkas(models.Model):
    """
    Berkas yang harus dicek (instance dari master list berkas).
    Tidak ada file upload, hanya status dan catatan.
    """
    permohonan = models.ForeignKey(Permohonan, on_delete=models.CASCADE, related_name="berkas")
    item = models.ForeignKey(BerkasItem, on_delete=models.CASCADE)

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('revisi', 'Revisi'),
        ('approved', 'Approved'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    last_updated = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        unique_together = ('permohonan', 'item')

    def __str__(self):
        return f"{self.item.nama} - {self.permohonan}"


# ----------------------------------------------------------------------
# CATATAN BERKAS
# ----------------------------------------------------------------------

class BerkasCatatan(models.Model):
    """
    Menampung catatan berulang pada setiap berkas.
    """
    permohonan_berkas = models.ForeignKey(PermohonanBerkas, on_delete=models.CASCADE, related_name="catatan")
    isi_catatan = models.TextField()
    dibuat_oleh = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    dibuat_pada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Catatan untuk {self.permohonan_berkas.item.nama}"
