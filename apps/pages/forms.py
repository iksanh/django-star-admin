from cProfile import label
from dataclasses import field, fields
from pyexpat import model
from django import forms
from django.forms import inlineformset_factory, widgets
from .models import Permohonan, Layanan, BerkasItem, District, Village, CatatanTemplate
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Row, Column
from crispy_forms.bootstrap import InlineCheckboxes

class PermohonanForm(forms.ModelForm):
    class Meta:
        model = Permohonan
        fields = ['nama_pemohon','atas_nama', 'nik', 'layanan', 'tanggal_permohonan', 'district','village']

        labels = {
            'district' : 'Kecamatan',
            'village': 'Desa'
        }
        widgets = {
            "nama_pemohon": forms.TextInput(attrs={"class": "big-input"}),
            "alamat": forms.Textarea(attrs={"class": "form-control", "rows": 1, }),
            "tanggal_permohonan": forms.DateInput(
                attrs={"type": "date",  "class": "form-control  date datepicker navbar-date-picker"}
            ),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 🔥 Filter hanya district yang regency_id = '75xx'
        self.fields['district'].queryset = District.objects.filter(
            regency_id="7503"
        )


        # 🔹 1. Village kosong dulu
        self.fields['village'].queryset = Village.objects.none()

        # 🔹 2. Jika user sudah pilih district → baru filter village
        if 'district' in self.data:
            try:
                district_id = self.data.get('district')
                self.fields['village'].queryset = Village.objects.filter(
                    district_id=district_id
                ).order_by('name')
            except:
                pass

        # 🔹 3. Jika edit form → tampilkan village sesuai instance
        elif self.instance.pk and self.instance.district:
            self.fields['village'].queryset = Village.objects.filter(
                district=self.instance.district
            )

class LayananForm(forms.ModelForm):
    class Meta:
        model = Layanan
        fields = ['nama', 'deskripsi']

class BerkasItemForm(forms.ModelForm):
    class Meta:
        model = BerkasItem
        fields = ['nama', 'layanan', 'catatan']
        widgets = {
            'catatan': forms.Textarea(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Tambahkan catatan jika diperlukan...',
                'style': 'height: 120px; resize: vertical;',  
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(Column('nama', css_class="mb-3")),
            InlineCheckboxes('layanan'),
            Row(Column('catatan')),
            Submit('submit', 'Simpan', css_class="btn btn-primary"),
        )

class CatatanTemplateForm(forms.ModelForm):
    class Meta:
        model = CatatanTemplate
        fields = ['teks', 'berkas']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # crispy form helper
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Row(
                Column('teks', css_class="mb-3"),
            ),

            # Checkbox layanan agar horizontal/rapi
            InlineCheckboxes('berkas'),

            Submit('submit', 'Simpan', css_class="btn btn-primary"),
        )