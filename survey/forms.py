from django import forms
from dal import autocomplete
from survey import models

class PasienForms(forms.ModelForm):
    class Meta:
        model = models.Pasien
        fields = (
            'nik', 'nocm', 'nama', 'jk',
            'tgl_lahir', 'id_tmp_lahir',
            'alamat', 'rt', 'rw', 'id_kelurahan',)
        widgets = {
            'id_kelurahan': autocomplete.ModelSelect2(
                url='kelurahan-autocomplete',
                forward=['kecamatan',],
                attrs={
                    # Set some placeholder
                    'data-placeholder': 'Pilih Alamat Kelurahan',
                    # Only trigger autocompletion after 3 characters have been typed
                    # 'data-minimum-input-length': 1,
                },
            ),
            'id_tmp_lahir': autocomplete.ModelSelect2(
                url='kotakab-autocomplete',
                forward=['provinsi',],
                attrs={
                    # Set some placeholder
                    'data-placeholder': 'Pilih Tempat Kelahiran',
                    # Only trigger autocompletion after 3 characters have been typed
                    # 'data-minimum-input-length': 1,
                },
            ),
        }


class RegistrasiForms(forms.ModelForm):
    class Meta:
        model = models.Registrasi
        exclude = ('created_at', 'updated_at', 'deleted_at',)


class PemakaianKamarForms(forms.ModelForm):
    class Meta:
        model = models.PemakaianKamar
        exclude = ('created_at', 'updated_at', 'deleted_at',)


class SurveiKepuasanMasyarakatForms(forms.ModelForm):
    class Meta:
        model = models.SurveiKepuasanMasyarakat
        exclude = ('created_at', 'updated_at', 'deleted_at',)