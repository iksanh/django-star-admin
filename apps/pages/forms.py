from django import forms
from django.forms import inlineformset_factory
from .models import Permohonan, PermohonanBerkas, BerkasCatatan, BerkasItem

class PermohonanForm(forms.ModelForm):
    class Meta:
        model = Permohonan
        fields = ['nama_pemohon', 'nik', 'layanan']


class PermohonanBerkasForm(forms.ModelForm):
    class Meta:
        model = PermohonanBerkas
        fields = ['status']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'})
        }


class BerkasCatatanForm(forms.ModelForm):
    class Meta:
        model = BerkasCatatan
        fields = ['isi_catatan']
        widgets = {
            'isi_catatan': forms.Textarea(attrs={'rows': 2})
        }


PermohonanBerkasFormSet = inlineformset_factory(
    Permohonan,
    PermohonanBerkas,
    form=PermohonanBerkasForm,
    extra=0,
    can_delete=False
)

BerkasCatatanFormSet = inlineformset_factory(
    PermohonanBerkas,
    BerkasCatatan,
    form=BerkasCatatanForm,
    extra=1,
    can_delete=False
)
