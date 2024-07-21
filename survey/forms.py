from django import forms
from dal import autocomplete
from survey import models

class KotakabForms(forms.ModelForm):
    class Meta:
        model = models.Kotakab
        fields = '__all__'
        widgets = {
            'id_provinsi': autocomplete.ModelSelect2(
                url='provinsi-autocomplete',
                # forward=['kotakab',],
                attrs={
                    # Set some placeholder
                    'data-placeholder': 'Pilih Provinsi',
                    # Only trigger autocompletion after 3 characters have been typed
                    # 'data-minimum-input-length': 1,
                },
            ),
        }
        

class KecamatanForms(forms.ModelForm):
    class Meta:
        model = models.Kecamatan
        fields = '__all__'
        widgets = {
            'id_kotakab': autocomplete.ModelSelect2(
                url='kotakab-autocomplete',
                # forward=['kotakab',],
                attrs={
                    # Set some placeholder
                    'data-placeholder': 'Pilih Kota/Kabupaten',
                    # Only trigger autocompletion after 3 characters have been typed
                    # 'data-minimum-input-length': 1,
                },
            ),
        }
        

class KelurahanForms(forms.ModelForm):
    class Meta:
        model = models.Kelurahan
        fields = '__all__'
        widgets = {
            'id_kecamatan': autocomplete.ModelSelect2(
                url='kecamatan-autocomplete',
                forward=['kotakab',],
                attrs={
                    # Set some placeholder
                    'data-placeholder': 'Pilih Kecamatan',
                    # Only trigger autocompletion after 3 characters have been typed
                    # 'data-minimum-input-length': 1,
                },
            ),
        }


class RuanganForms(forms.ModelForm):
    class Meta:
        model = models.Ruangan
        fields = '__all__'
        widgets = {
            'id_instalasi': autocomplete.ModelSelect2(
                url='instalasi-autocomplete',
                # forward=['kotakab',],
                attrs={
                    # Set some placeholder
                    'data-placeholder': 'Pilih Instalasi',
                    # Only trigger autocompletion after 3 characters have been typed
                    # 'data-minimum-input-length': 1,
                },
            ),
        }


class KamarForms(forms.ModelForm):
    class Meta:
        model = models.Kamar
        fields = '__all__'
        widgets = {
            'id_ruangan': autocomplete.ModelSelect2(
                url='ruangan-autocomplete',
                # forward=['kotakab',],
                attrs={
                    # Set some placeholder
                    'data-placeholder': 'Pilih Ruangan',
                    # Only trigger autocompletion after 3 characters have been typed
                    # 'data-minimum-input-length': 1,
                },
            ),
        }


class TempatTidurForms(forms.ModelForm):
    class Meta:
        model = models.TempatTidur
        fields = '__all__'
        widgets = {
            'id_kamar': autocomplete.ModelSelect2(
                url='kamar-autocomplete',
                # forward=['kotakab',],
                attrs={
                    # Set some placeholder
                    'data-placeholder': 'Pilih Kamar',
                    # Only trigger autocompletion after 3 characters have been typed
                    # 'data-minimum-input-length': 1,
                },
            ),
        }


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
        widgets = {
            'norm': autocomplete.ModelSelect2(
                url='pasien-autocomplete',
                # forward=['kotakab',],
                attrs={
                    # Set some placeholder
                    'data-placeholder': 'Ketik Nama/NoRM/NIK',
                    # Only trigger autocompletion after 3 characters have been typed
                    # 'data-minimum-input-length': 1,
                },
            ),
            'id_kelas': autocomplete.ModelSelect2(
                url='kelaspelayanan-autocomplete',
                # forward=['kotakab',],
                attrs={
                    # Set some placeholder
                    'data-placeholder': 'Pilih Kelas Pelayanan',
                    # Only trigger autocompletion after 3 characters have been typed
                    # 'data-minimum-input-length': 1,
                },
            ),
        }


class PemakaianKamarForms(forms.ModelForm):
    class Meta:
        model = models.PemakaianKamar
        exclude = ('created_at', 'updated_at', 'deleted_at',)
        widgets = {
            'id_registrasi': autocomplete.ModelSelect2(
                url='registrasi-autocomplete',
                # forward=['kotakab',],
                attrs={
                    # Set some placeholder
                    'data-placeholder': 'Ketik Nama/NoRM/NIK/No.Registrasi',
                    # Only trigger autocompletion after 3 characters have been typed
                    # 'data-minimum-input-length': 1,
                },
            ),
            'id_tempattidur': autocomplete.ModelSelect2(
                url='tempattidur-autocomplete',
                # forward=['kotakab',],
                attrs={
                    # Set some placeholder
                    'data-placeholder': 'Pilih Tempat Tidur',
                    # Only trigger autocompletion after 3 characters have been typed
                    # 'data-minimum-input-length': 1,
                },
            ),
        }


class SurveiKepuasanMasyarakatForms(forms.ModelForm):
    class Meta:
        model = models.SurveiKepuasanMasyarakat
        exclude = ('created_at', 'updated_at', 'deleted_at',)