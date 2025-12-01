from dataclasses import field
from django import forms
from django.forms import inlineformset_factory, widgets
from .models import Permohonan, Layanan, BerkasItem

class PermohonanForm(forms.ModelForm):
    class Meta:
        model = Permohonan
        fields = ['nama_pemohon', 'nik', 'layanan', 'tanggal_permohonan', 'alamat']
        widgets = {
            "nama_pemohon": forms.TextInput(attrs={"class": "big-input"}),
            "alamat": forms.Textarea(attrs={"class": "form-control", "rows": 1, }),
            "tanggal_permohonan": forms.DateInput(
                attrs={"type": "date",  "class": "form-control  date datepicker navbar-date-picker"}
            ),
        }


class LayananForm(forms.ModelForm):
    class Meta:
        model = Layanan
        fields = ['nama', 'deskripsi']

class BerkasItemForm(forms.ModelForm):
    class Meta:
         model = BerkasItem
         fields = ['nama']