from dal import autocomplete
from django.db.models import Q
from survey.models import (
    Kelurahan, Kotakab, Kecamatan, Provinsi,
    Instalasi, Ruangan, Kamar, TempatTidur,
    Pasien, KelasPelayanan, Registrasi
)


class KelasPelayananAutocomplete(autocomplete.Select2QuerySetView):
    class Meta:
        model = KelasPelayanan

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return KelasPelayanan.objects.none()
        qs = KelasPelayanan.objects.using('default').all()
        if self.q:
            qs = qs.filter(nama__icontains=self.q)
        return qs


class PasienAutocomplete(autocomplete.Select2QuerySetView):
    class Meta:
        model = Pasien

    def get_result_value(self, result: Pasien):
        """Return the value of a result."""
        return str(result.nocm)

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Pasien.objects.none()
        qs = Pasien.objects.using('default').all()
        if self.q:
            qs = qs.filter(
                Q(nama__icontains=self.q)
                | Q(nocm__icontains=self.q)
                | Q(nik__icontains=self.q)
            )
        return qs
    

class RegistrasiAutocomplete(autocomplete.Select2QuerySetView):
    class Meta:
        model = Registrasi

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Registrasi.objects.none()
        qs = Registrasi.objects.using('default').all()
        if self.q:
            qs = qs.filter(
                Q(id=self.q)
                | Q(norm__nocm__icontains=self.q)
                | Q(norm__nik__icontains=self.q)
                | Q(norm__nama__icontains=self.q)
            )
        return qs


class InstalasiAutocomplete(autocomplete.Select2QuerySetView):
    class Meta:
        model = Instalasi

    def get_queryset(self):
        qs = Instalasi.objects.using('default').all()
        if self.q:
            qs = qs.filter(nama__icontains=self.q)
        return qs


class RuanganAutocomplete(autocomplete.Select2QuerySetView):
    class Meta:
        model = Ruangan

    def get_queryset(self):
        qs = Ruangan.objects.using('default').all()
        if self.q:
            qs = qs.filter(
                Q(nama__icontains=self.q))
        return qs
    

class KamarAutocomplete(autocomplete.Select2QuerySetView):
    class Meta:
        model = Kamar

    def get_queryset(self):
        qs = Kamar.objects.using('default').all()
        if self.q:
            qs = qs.filter(
                Q(nama__icontains=self.q)
                | Q(id_ruangan__nama__icontains=self.q),
            )
        return qs
    

class TempatTidurAutocomplete(autocomplete.Select2QuerySetView):
    class Meta:
        model = TempatTidur

    def get_queryset(self):
        qs = TempatTidur.objects.using('default').all()
        if self.q:
            qs = qs.filter(
                Q(nama__icontains=self.q)
                # | Q(id_kamar__nama__icontains=self.q)
                | Q(id_kamar__id_ruangan__nama__icontains=self.q)
            )
        return qs


class ProvinsiAutocomplete(autocomplete.Select2QuerySetView):
    class Meta:
        model = Provinsi

    def get_queryset(self):
        qs = Provinsi.objects.using('default').all()
        id_provinsi = self.forwarded.get(
            'id_provinsi', None
        ) or self.forwarded.get(
            'provinsi_asal', None
        ) or self.forwarded.get(
            'provinsi_tujuan', None
        ) or self.forwarded.get(
            'provinsi_lahir', None
        ) or self.forwarded.get('provinsi', None)
        if id_provinsi:
            qs = Provinsi.objects.using('default').filter(
                id_provinsi=id_provinsi).order_by('-nama')
        if self.q:
            qs = qs.filter(nama__icontains=self.q)

        return qs
    

class KotaKabAutocomplete(autocomplete.Select2QuerySetView):
    class Meta:
        model = Kotakab

    def get_queryset(self):
        qs = Kotakab.objects.using('default').all()
        id_provinsi = self.forwarded.get(
            'id_provinsi', None
        ) or self.forwarded.get(
            'provinsi_asal', None
        ) or self.forwarded.get(
            'provinsi_tujuan', None
        ) or self.forwarded.get(
            'provinsi_lahir', None
        ) or self.forwarded.get('provinsi', None)
        if id_provinsi:
            qs = Kotakab.objects.using('default').filter(
                id_provinsi=id_provinsi).order_by('-nama')
        if self.q:
            qs = qs.filter(nama__icontains=self.q)

        return qs
    

class KecamatanAutocomplete(autocomplete.Select2QuerySetView):
    class Meta:
        model = Kecamatan

    def get_queryset(self):
        qs = Kecamatan.objects.using('default').all()
        id_kota = self.forwarded.get('id_kota', None)
        id_provinsi = self.forwarded.get(
            'id_provinsi', None
        ) or self.forwarded.get(
            'provinsi_asal', None
        ) or self.forwarded.get(
            'provinsi_tujuan', None
        ) or self.forwarded.get(
            'provinsi_lahir', None
        ) or self.forwarded.get('provinsi', None)
        if id_provinsi:
            qs = Kecamatan.objects.using('default').filter(
                id_kotakab__id_provinsi=id_provinsi).order_by('-nama')
        if id_kota:
            qs = Kecamatan.objects.using('default').filter(
                id_kotakab=id_kota).order_by('-nama')
        if self.q:
            qs = qs.filter(
                Q(nama__icontains=self.q)
                | Q(id_kotakab__nama__icontains=self.q)
                | Q(id_kotakab__id_provinsi__nama__icontains=self.q)
            )

        return qs


class KelurahanAutocomplete(autocomplete.Select2QuerySetView):
    class Meta:
        model = Kelurahan

    def get_queryset(self):
        qs = Kelurahan.objects.using('default').all()
        id_provinsi = self.forwarded.get('id_provinsi', None)
        id_kota = self.forwarded.get('id_kota', None)
        id_kecamatan = self.forwarded.get(
            'id_kecataman', None
        ) or self.forwarded.get(
            'kecamatan_asal', None
        ) or self.forwarded.get(
            'kecamatan_tujuan', None
        ) or self.forwarded.get('kecamatan', None)
        if id_provinsi:
            qs = Kelurahan.objects.using('default').filter(
                id_provinsi=id_provinsi).order_by('-nama')
        if id_kota:
            qs = Kelurahan.objects.using('default').filter(
                id_kecamatan__id_kotakab=id_kota).order_by('-nama')
        if id_kecamatan:
            qs = Kelurahan.objects.using('default').filter(
                id_kecamatan=id_kecamatan).order_by('-nama')
        if self.q:
            qs = qs.filter(
                Q(nama__icontains=self.q) 
                | Q(id_kecamatan__nama__icontains=self.q)
                | Q(id_kecamatan__id_kotakab__nama__icontains=self.q)
                | Q(id_kecamatan__id_kotakab__id_provinsi__nama__icontains=self.q)
            )

        return qs
