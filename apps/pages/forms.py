from dataclasses import field
from django import forms
from django.forms import inlineformset_factory, widgets
from .models import Permohonan, Layanan, BerkasItem
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Row, Column
from crispy_forms.bootstrap import InlineCheckboxes

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
        fields = ['nama', 'layanan']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # crispy form helper
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Row(
                Column('nama', css_class="mb-3"),
            ),

            # Checkbox layanan agar horizontal/rapi
            InlineCheckboxes('layanan'),

            Submit('submit', 'Simpan', css_class="btn btn-primary"),
        )