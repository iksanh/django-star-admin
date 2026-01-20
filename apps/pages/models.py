from django.db import models
from django.contrib.auth import get_user_model
from simple_history.models import HistoricalRecords

User = get_user_model()



class Province(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=2
    )
    name = models.CharField(
        max_length=255
    )

    class Meta:
        db_table = 'reg_provinces'   # supaya sesuai dengan tabel SQL
        verbose_name = "Province"
        verbose_name_plural = "Provinces"

    def __str__(self):
        return self.name


class Regency(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=4
    )
    province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
        db_column='province_id'
    )
    name = models.CharField(
        max_length=255
    )

    class Meta:
        db_table = 'reg_regencies'

    def __str__(self):
        return self.name

class District(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=6
    )
    regency = models.ForeignKey(
        Regency,
        on_delete=models.CASCADE,
        db_column='regency_id'
    )
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'reg_districts'

    def __str__(self):
        return self.name

class Village(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=10
    )
    district = models.ForeignKey(
        District,
        on_delete=models.CASCADE,
        db_column='district_id'
    )
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'reg_villages'

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
    layanan = models.ManyToManyField(Layanan, related_name="berkas_items")

      # urutan berbeda per jenis hak / layanan
    urutan = models.JSONField(
        default=dict,
        blank=True,
        help_text="Contoh: {'HM': 3, 'HGB': 4}"
    )
    catatan = models.TextField(null=True, blank=True)
 
    def get_urutan(self, kode_layanan):
        """
        Ambil urutan sesuai jenis hak (HM/HGB/HGU)
        """
        return self.urutan.get(kode_layanan, 999)

    
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
    atas_nama = models.CharField(max_length=255, null=True, blank=True)
    nik = models.CharField(max_length=50, null=True, blank=True)
   
    # ganti alamat ke relasi
    district = models.ForeignKey(
        District,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    village = models.ForeignKey(
        Village,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    layanan = models.ForeignKey(Layanan, on_delete=models.CASCADE)
    tanggal_permohonan = models.DateField()

    #add history 
    history = HistoricalRecords()
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


