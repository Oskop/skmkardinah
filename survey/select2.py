from dal import autocomplete
from django.db.models import Q
from survey.models import Kelurahan, Kotakab


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
