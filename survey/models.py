from django.db import models
from datetime import datetime


# class Agama(models.Model):
#     id = models.CharField(primary_key=True, max_length=1)
#     nama = models.CharField(max_length=11, blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'agama'
#         verbose_name = 'Agama'
#         verbose_name_plural = 'Agama'

#     def __str__(self):
#         return self.nama


# class GolonganDarah(models.Model):
#     id = models.CharField(primary_key=True, max_length=2)
#     nama = models.CharField(max_length=10, blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'golongan_darah'
#         verbose_name = 'Golongan Darah'
#         verbose_name_plural = 'Golongan Darah'

#     def __str__(self):
#         return r"{}".format(self.nama)


# class Pendidikan(models.Model):
#     id = models.CharField(primary_key=True, max_length=2)
#     nama = models.CharField(max_length=35, blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'pendidikan'
#         verbose_name = 'Pendidikan'
#         verbose_name_plural = 'Pendidikan'

#     def __str__(self):
#         return r"{}".format(self.nama)


# class Pekerjaan(models.Model):
#     id = models.CharField(primary_key=True, max_length=2)
#     pekerjaan = models.CharField(max_length=50, blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = "pekerjaan"
#         verbose_name = "Pekerjaan"
#         verbose_name_plural = "Pekerjaan"

#     def __str__(self):
#         return f"{self.pekerjaan}"


# class StatusKawin(models.Model):
#     id = models.CharField(primary_key=True, max_length=1)
#     nama = models.CharField(max_length=11)

#     def __str__(self) -> str:
#         return f"{self.nama}"

#     class Meta:
#         managed = True
#         db_table = 'status_kawin'
#         verbose_name = 'Status Kawin'
#         verbose_name_plural = 'Status-Status Kawin'


# class StatusHubunganKeluarga(models.Model):
#     id = models.CharField(max_length=2, primary_key=True)
#     nama = models.CharField(max_length=15)

#     def __str__(self) -> str:
#         return f"{self.nama}"

#     class Meta:
#         managed = True
#         db_table = 'status_hub_keluarga'
#         verbose_name = 'Status Hubungan Keluarga'
#         verbose_name_plural = 'Status-Status Hubungan Keluarga'


class Kecamatan(models.Model):
    id = models.CharField(primary_key=True, max_length=7)
    id_kotakab = models.ForeignKey(
        'Kotakab', models.DO_NOTHING, db_column='id_kotakab',
        blank=True, null=True, verbose_name="Kota/Kabupaten")
    # nama = models.CharField(max_length=-1, blank=True, null=True)
    nama = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'kecamatan'
        verbose_name = 'Kecamatan'
        verbose_name_plural = 'Kecamatan'

    def __str__(self):
        return r"{}".format(self.nama)


class Kelurahan(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    id_kecamatan = models.ForeignKey(
        Kecamatan, models.DO_NOTHING, db_column='id_kecamatan',
        blank=True, null=True, verbose_name='Kecamatan')
    # nama = models.CharField(max_length=-1, blank=True, null=True)
    nama = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'kelurahan'
        verbose_name = 'Kelurahan'
        verbose_name_plural = 'Kelurahan'

    def __str__(self):
        return r"{}, {}, {}".format(
            self.nama, self.id_kecamatan.nama,
            self.id_kecamatan.id_kotakab.nama)


class Kotakab(models.Model):
    id = models.CharField(primary_key=True, max_length=4)
    id_provinsi = models.ForeignKey(
        'Provinsi', models.DO_NOTHING, db_column='id_provinsi',
        blank=True, null=True, verbose_name="Provinsi")
    # nama = models.CharField(max_length=-1, blank=True, null=True)
    nama = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'kotakab'
        verbose_name = 'Kota Kabupaten'
        verbose_name_plural = 'Kota Kabupaten'

    def __str__(self):
        return r"{}".format(self.nama)


class Provinsi(models.Model):
    id = models.CharField(primary_key=True, max_length=2)
    # nama = models.CharField(max_length=-1, blank=True, null=True)
    nama = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'provinsi'
        verbose_name = 'Provinsi'
        verbose_name_plural = 'Provinsi'

    def __str__(self):
        return r"{}".format(self.nama)


class Pasien(models.Model):
    """Pasien Model

    Args:
        models (**kwargs): defined attribute[
            nik: CharField(primary_key=True, max_length=16)
            nocm: CharField(max_length=7, unique=True,
                                    db_column="nocm")
            jk: CharField(max_length=1, blank=True, null=True)
            id_tmp_lahir: ForeignKey(
                Kotakab, models.DO_NOTHING, db_column='id_tmp_lahir',
                blank=True, null=True)
            tgl_lahir: DateTimeField(blank=True, null=True)
            alamat: TextField(blank=True, null=True)
            rt: CharField(max_length=2, blank=True, null=True)
            rw: CharField(max_length=2, blank=True, null=True)
            id_kelurahan: ForeignKey(
                Kelurahan, models.DO_NOTHING, db_column='id_kelurahan',
                blank=True, null=True)
            created_at: DateTimeField(blank=True, null=True)
            deleted_at: DateTimeField(blank=True, null=True)
            nama: CharField(max_length=60, blank=True, null=True)
            updated_at: DateTimeField(blank=True, null=True)
        ]

    Returns:
        _type_: _description_
    """
    nik = models.CharField(primary_key=True, max_length=16)
    nocm = models.CharField(max_length=7, unique=True, db_column="nocm")
    jk = models.CharField(max_length=1, blank=True, null=True)
    id_tmp_lahir = models.ForeignKey(
        Kotakab, models.DO_NOTHING, db_column='id_tmp_lahir',
        blank=True, null=True, verbose_name="Tempat Lahir")
    tgl_lahir = models.DateTimeField(
        blank=True, null=True, verbose_name="Tanggal Lahir")
    # id_agama = models.ForeignKey(
    #     Agama, models.DO_NOTHING, db_column='id_agama', blank=True, null=True)
    # alamat = models.CharField(max_length=-1, blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)
    rt = models.CharField(max_length=2, blank=True, null=True)
    rw = models.CharField(max_length=2, blank=True, null=True)
    id_kelurahan = models.ForeignKey(
        Kelurahan, models.DO_NOTHING, db_column='id_kelurahan',
        blank=True, null=True, verbose_name="Kelurahan")
    # kode_pos = models.CharField(max_length=5, blank=True, null=True)
    # id_pekerjaan = models.ForeignKey(
    #     Pekerjaan, models.DO_NOTHING, db_column='id_pekerjaan',
    #     blank=True, null=True)
    # id_pendidikan = models.ForeignKey(
    #     Pendidikan, models.DO_NOTHING, db_column='id_pendidikan',
    #     blank=True, null=True)
    # kewarganegaraan = models.CharField(
    #     max_length=3, blank=True, null=True)
    # status_kawin = models.CharField(max_length=11, blank=True, null=True)
    # ini = models.CharField(max_length=1, blank=True, null=True)
    # status_kawin_id = models.ForeignKey(
    #     'StatusKawin', models.DO_NOTHING, blank=True, null=True,
    #     db_column='status_kawin_id')
    # status_hub_kel = models.CharField(max_length=15, blank=True, null=True)
    # status_hub_kel_id = models.ForeignKey(
    #     'StatusHubunganKeluarga', models.DO_NOTHING,
    #     blank=True, null=True,
    #     db_column='status_hub_kel_id')
    # no_akta_kawin = models.CharField(max_length=22, blank=True, null=True)
    # no_akta_cerai = models.CharField(max_length=22, blank=True, null=True)
    # ayah = models.CharField(max_length=60, blank=True, null=True)
    # ibu = models.CharField(max_length=60, blank=True, null=True)
    # id_goldar = models.ForeignKey(
    #     GolonganDarah, models.DO_NOTHING, db_column='id_goldar',
    #     blank=True, null=True)
    nama = models.CharField(max_length=60, blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.nocm} {self.nama}"

    class Meta:
        managed = True
        db_table = 'pasien'
        verbose_name = 'Pasien'
        verbose_name_plural = 'Pasien-Pasien'

    def __str__(self):
        return r"{}".format(self.nama)


# Rumah Sakit
class Instalasi(models.Model):
    """Instalasi Model

    Args:
        models (**kwargs): (
            nama: str(30)
        )
    """
    id = models.CharField(primary_key=True, max_length=2, db_column="id")
    nama = models.CharField(max_length=30, db_column="nama")

    def __str__(self) -> str:
        return f"{self.id} {self.nama}"
    class Meta:
        managed = True
        db_table = "instalasi"
        verbose_name = "Instalasi"
        verbose_name_plural = "Instalasi-Instalasi"


class Ruangan(models.Model):
    """Ruangan Model

    Args:
        models (**kwargs): (
            nama: str(30),
            id_instalasi: Instalasi
        )
    """
    id = models.CharField(primary_key=True, max_length=3, db_column="id")
    nama = models.CharField(max_length=30, db_column="nama")
    id_instalasi = models.ForeignKey(
        Instalasi, models.DO_NOTHING, db_column="id_instalasi",
        verbose_name="Instalasi")
    
    def __str__(self) -> str:
        return f"{self.nama}"

    class Meta:
        managed = True
        db_table = "ruangan"
        verbose_name = "Ruangan"
        verbose_name_plural = "Ruangan-Ruangan"


class Kamar(models.Model):
    """Kamar Model

    Args:
        models (**kwargs): (
            nama: str(30),
            id_ruangan: Ruangan
        )
    """
    id = models.CharField(primary_key=True, max_length=4, db_column="id")
    nama = models.CharField(max_length=30, db_column="nama")
    id_ruangan = models.ForeignKey(
        Ruangan, models.DO_NOTHING, db_column="id_ruangan",
        verbose_name="Ruangan")
    
    def __str__(self) -> str:
        return f"{self.id_ruangan.nama}, {self.nama}"

    class Meta:
        managed = True
        db_table = "kamar"
        verbose_name = "Kamar"
        verbose_name_plural = "Kamar-Kamar"


class TempatTidur(models.Model):
    """Tempat Tidur Model

    Args:
        models (**kwargs): (
            nama: str(10),
            id_kamar: Kamar
        )
    """
    id = models.CharField(primary_key=True, max_length=4, db_column="id")
    nama = models.CharField(max_length=10, db_column="nama")
    id_kamar = models.ForeignKey(
        Kamar, models.DO_NOTHING, db_column="id_kamar",
        verbose_name="Kamar")
    
    def __str__(self) -> str:
        return str(f"{self.nama}, {self.id_kamar.nama}, "
                   + f"{self.id_kamar.id_ruangan.nama}")

    class Meta:
        managed = True
        db_table = "tempat_tidur"
        verbose_name = "Tempat Tidur"
        verbose_name_plural = "Tempat-Tempat Tidur"


# class Penjamin(models.Model):
#     id = models.CharField(primary_key=True, max_length=2, db_column="id")
#     nama = models.CharField(max_length=30, db_column="nama")

#     class Meta:
#         managed = True
#         db_table = "penjamin"
#         verbose_name = "Penjamin"
#         verbose_name_plural = "Para Penjamin"


class KelasPelayanan(models.Model):
    """Kelas Pelayanan Model

    Args:
        models (**kwargs): (
            nama: str(10)
        )
    """
    id = models.CharField(primary_key=True, max_length=2, db_column="id")
    nama = models.CharField(max_length=10, db_column="nama")

    def __str__(self) -> str:
        return f"{self.nama}"

    class Meta:
        managed = True
        db_table = "kelas_pelayanan"
        verbose_name = "Kelas Pelayanan"
        verbose_name_plural = "Kelas-Kelas Pelayanan"


class JenisPegawai(models.Model):
    """Jenis Pegawai Model

    Args:
        models (**kwargs): (
            nama: str(10)
        )
    """
    id = models.CharField(primary_key=True, max_length=2, db_column="id")
    nama = models.CharField(max_length=20, db_column="nama")

    def __str__(self) -> str:
        return f"{self.nama}"

    class Meta:
        managed = True
        db_table = "jenis_pegawai"
        verbose_name = "Jenis Pegawai"
        verbose_name_plural = "Jenis-Jenis Pegawai"


class Layanan(models.Model):
    """Layanan Model

    Args:
        models (**kwargs): (
            nama: str(10)

        )
    """
    id = models.CharField(primary_key=True, max_length=6, db_column="id")
    nama = models.CharField(max_length=50, db_column="nama")

    def __str__(self) -> str:
        return f"{self.nama}"

    class Meta:
        managed = True
        db_table = "layanan"
        verbose_name = "Layanan"
        verbose_name_plural = "Layanan-Layanan"


class Pegawai(models.Model):
    """Pegawai Model

    Args:
        models (**kwargs): (
            id: str(10),
            nama: str(50),
            jenis_pegawai: JenisPegawai,
        )
    """
    id = models.CharField(primary_key=True, max_length=10, db_column="id")
    nama = models.CharField(max_length=50, db_column="nama")
    jenis_pegawai = models.ForeignKey(
        JenisPegawai, models.DO_NOTHING,
        blank=True, null=True, verbose_name="Jenis Pegawai")
    
    created_at = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.nama}"

    class Meta:
        managed = True
        db_table = "pegawai"
        verbose_name = "Pegawai"
        verbose_name_plural = "Direktur"


class Registrasi(models.Model):
    """Registrasi Model

    Args:
        
        models (**kwargs): {
            id: int,
            norm: Pasien,
            id_kelas: KelasPelayanan,
            tglregistrasi: datetime,
            tglpulang: datetime|nullable,
        }
    """
    id = models.AutoField(primary_key=True, db_column="id")
    norm = models.ForeignKey(
        Pasien, models.DO_NOTHING, 
        db_column="id_pasien", to_field='nocm',
        verbose_name="Pasien")
    # id_penjamin = models.ForeignKey(
    #     Penjamin, models.DO_NOTHING, db_column="id_penjamin")
    id_kelas = models.ForeignKey(
        KelasPelayanan, models.DO_NOTHING, db_column="id_kelas",
        verbose_name="Kelas Pelayanan")
    tglregistrasi = models.DateTimeField(
        db_column="tglpendaftaran", verbose_name="Tanggal Registrasi")
    tglpulang = models.DateTimeField(
        db_column="tglpulang", null=True, blank=True,
        verbose_name="Tanggal Pulang")

    created_at = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return f"No. Reg. {self.id}"

    class Meta:
        managed = True
        db_table = "registrasi"
        verbose_name = "Registrasi"
        verbose_name_plural = "Registrasi"


class PemakaianKamar(models.Model):
    """Pemakaian Kamar Model

    Args:
        models (**kwargs): (
            id_registrasi: Registrasi
            tglmasuk: datetime
            tglkeluar: datetime
            id_tempattidur: TempatTidur
    """
    id = models.AutoField(primary_key=True, db_column="id")
    id_registrasi = models.ForeignKey(
        Registrasi, models.DO_NOTHING, db_column="id_pendaftaran",
        verbose_name="Nomor Registrasi")
    tglmasuk = models.DateTimeField(
        auto_now_add=True, verbose_name="Tanggal Masuk")
    tglkeluar = models.DateTimeField(
        blank=True, null=True, verbose_name="Tanggal Keluar")
    id_tempattidur = models.ForeignKey(
        TempatTidur, models.DO_NOTHING, db_column='id_tempattidur',
        verbose_name="Tempat Tidur")
    
    created_at = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    class Meta:
        managed = True
        db_table = "pemakaian_kamar"
        verbose_name = "Pemakaian Kamar"
        verbose_name_plural = "Riwayat Pemakaian Kamar"


class Pelayanan(models.Model):
    """Pelayanan yang diberikan kepada pasien Model

    Args:
        models (**kwargs): (
            id_registrasi: Registrasi,
            tgllayanan: datetime,
            id_pegawai: Pegawai,
            id_layanan: Layanan,
            id_pemakaiankamar: PemakaianKamar,
    """
    id = models.AutoField(primary_key=True, db_column="id")
    id_registrasi = models.ForeignKey(
        Registrasi, models.DO_NOTHING, db_column="id_pendaftaran",
        verbose_name="Nomor Registrasi")
    tgllayanan = models.DateTimeField(
        blank=True, null=True, verbose_name="Tanggal Layanan")
    id_pegawai = models.ForeignKey(
        Pegawai, models.DO_NOTHING,
        blank=True, null=True, verbose_name="Petugas")
    id_layanan = models.ForeignKey(
        Layanan, models.DO_NOTHING, blank=True, null=True,
        verbose_name="Layanan")
    id_pemakaiankamar = models.ForeignKey(
        PemakaianKamar, models.DO_NOTHING, blank=True, null=True,
        verbose_name="Lokasi")
    

    created_at = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = True
        db_table = "pelayanan"
        verbose_name = "Pelayanan"
        verbose_name_plural = "Pelayanan"


class SurveiKepuasanMasyarakat(models.Model):
    """Survei Kepuasan Masyarakat

    Args:
        models (**kwargs): (
            id_registrasi: Registrasi,
            fasilitas_rate: int,
            perawat_rate: int,
            dokter_rate: int,
            farmasi_rate: int,
            komentar: str(-1)
        )
    """
    id = models.AutoField(primary_key=True, db_column='id')
    id_registrasi = models.ForeignKey(
        Registrasi, models.DO_NOTHING, db_column="id_pendaftaran",
        verbose_name="Nomor Registrasi")
    fasilitas_rate = models.IntegerField()
    perawat_rate = models.IntegerField()
    dokter_rate = models.IntegerField()
    farmasi_rate = models.IntegerField()
    komentar = models.TextField(blank=True, null=True)
    komentar_suara = models.FileField(upload_to='survey/voices/',
                                      null=True)

    created_at = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    class Meta:
        managed = True
        db_table = "survei"
        verbose_name = "Survei"
        verbose_name_plural = "Survei-Survei"


class SurveiKepuasanMasyarakatRev(models.Model):
    """Survei Kepuasan Masyarakat

    Args:
        models (**kwargs): (
            id_registrasi: Registrasi,
            fasilitas_rate: int,
            perawat_rate: int,
            dokter_rate: int,
            farmasi_rate: int,
            komentar: str(-1)
        )
    """
    id = models.AutoField(primary_key=True, db_column='id')
    id_registrasi = models.ForeignKey(
        Registrasi, models.DO_NOTHING, db_column="id_pendaftaran",
        verbose_name="Nomor Registrasi")

    etika_perawat_rate = models.SmallIntegerField(default=0)
    penampilan_perawat_rate = models.SmallIntegerField(default=0)
    kecakapan_perawat_rate = models.SmallIntegerField(default=0)
    ketepatan_perawat_rate = models.SmallIntegerField(default=0)
    komunikatif_perawat_rate = models.SmallIntegerField(default=0)
    komentar_perawat = models.TextField(blank=True, null=True)
    komentar_perawat_suara = models.FileField(upload_to='survey/voices/perawat/',
                                              null=True)
    perawat_time_critic = models.DateTimeField(blank=True, null=True)

    etika_dokter_rate = models.SmallIntegerField(default=0)
    penampilan_dokter_rate = models.SmallIntegerField(default=0)
    kecakapan_dokter_rate = models.SmallIntegerField(default=0)
    ketepatan_dokter_rate = models.SmallIntegerField(default=0)
    solutif_dokter_rate = models.SmallIntegerField(default=0)
    komentar_dokter = models.TextField(blank=True, null=True)
    komentar_dokter_suara = models.FileField(upload_to='survey/voices/dokter/',
                                             null=True)
    dokter = models.ForeignKey(
        Pegawai, models.DO_NOTHING, blank=True, null=True)

    etika_farmasi_rate = models.SmallIntegerField(default=0)
    penampilan_farmasi_rate = models.SmallIntegerField(default=0)
    kecepatan_farmasi_rate = models.SmallIntegerField(default=0)
    ketepatan_farmasi_rate = models.SmallIntegerField(default=0)
    informatif_farmasi_rate = models.SmallIntegerField(default=0)
    komentar_farmasi = models.TextField(blank=True, null=True)
    komentar_farmasi_suara = models.FileField(upload_to='survey/voices/farmasi/',
                                              null=True)

    kelengkapan_fasilitas_rate = models.SmallIntegerField(default=0)
    kebersihan_fasilitas_rate = models.SmallIntegerField(default=0)
    kenyamanan_fasilitas_rate = models.SmallIntegerField(default=0)
    kamarmandi_fasilitas_rate = models.SmallIntegerField(default=0)
    kualitas_fasilitas_rate = models.SmallIntegerField(default=0)
    komentar_fasilitas = models.TextField(blank=True, null=True)
    komentar_fasilitas_suara = models.FileField(upload_to='survey/voices/fasilitas/',
                                                null=True)

    created_at = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = True
        db_table = "survei_rev"
        verbose_name = "Survei Kepuasan Masyarakat"
        verbose_name_plural = "Survei-Survei Kepuasan Masyarakat"



# class SKMPerawat(models.Model):
#     """Survei Kepuasan Masyarakat - Perawat

#     Args:
#         models (**kwargs): (
#             id_registrasi: Registrasi,
#             etika_rate: int,
#             penampilan_rate: int,
#             kecakapan_rate: int,
#             ketepatan_rate: int,
#             komunikatif_rate: int,
#             komentar: str(-1),
#             komentar_suara: FileField
#         )
#     """
#     id = models.AutoField(primary_key=True, db_column='id')
#     id_registrasi = models.ForeignKey(
#         Registrasi, models.DO_NOTHING, db_column="id_pendaftaran",
#         verbose_name="Nomor Registrasi")
#     etika_rate = models.SmallIntegerField()
#     penampilan_rate = models.SmallIntegerField()
#     kecakapan_rate = models.SmallIntegerField()
#     ketepatan_rate = models.SmallIntegerField()
#     komunikatif_rate = models.SmallIntegerField()
#     komentar_perawat = models.TextField(blank=True, null=True)
#     komentar_perawat_suara = models.FileField(upload_to='survey/voices/perawat/',
#                                       null=True)

#     created_at = models.DateTimeField(
#         auto_now_add=True, blank=True, null=True)
#     deleted_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
#     class Meta:
#         managed = True
#         db_table = "survei_perawat"
#         verbose_name = "Survei Perawat"
#         verbose_name_plural = "Survei Perawat-Perawat"


# class SKMDokter(models.Model):
#     """Survei Kepuasan Masyarakat - Dokter

#     Args:
#         models (**kwargs): (
#             id_registrasi: Registrasi,
#             etika_rate: int,
#             penampilan_rate: int,
#             kecakapan_rate: int,
#             ketepatan_rate: int,
#             solutif_rate: int,
#             komentar: str(-1),
#             komentar_suara: FileField
#         )
#     """
#     id = models.AutoField(primary_key=True, db_column='id')
#     id_registrasi = models.ForeignKey(
#         Registrasi, models.DO_NOTHING, db_column="id_pendaftaran",
#         verbose_name="Nomor Registrasi")
#     etika_rate = models.SmallIntegerField()
#     penampilan_rate = models.SmallIntegerField()
#     kecakapan_rate = models.SmallIntegerField()
#     ketepatan_rate = models.SmallIntegerField()
#     solutif_rate = models.SmallIntegerField()
#     komentar_dokter = models.TextField(blank=True, null=True)
#     komentar_dokter_suara = models.FileField(upload_to='survey/voices/dokter/',
#                                       null=True)

#     created_at = models.DateTimeField(
#         auto_now_add=True, blank=True, null=True)
#     deleted_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
#     class Meta:
#         managed = True
#         db_table = "survei_dokter"
#         verbose_name = "Survei Dokter"
#         verbose_name_plural = "Survei Dokter-Dokter"


# class SKMFarmasi(models.Model):
#     """Survei Kepuasan Masyarakat - Farmasi

#     Args:
#         models (**kwargs): (
#             id_registrasi: Registrasi,
#             etika_rate: int,
#             penampilan_rate: int,
#             kecepatan_rate: int,
#             ketepatan_rate: int,
#             informatif_rate: int,
#             komentar: str(-1),
#             komentar_suara: FileField
#         )
#     """
#     id = models.AutoField(primary_key=True, db_column='id')
#     id_registrasi = models.ForeignKey(
#         Registrasi, models.DO_NOTHING, db_column="id_pendaftaran",
#         verbose_name="Nomor Registrasi")
#     etika_rate = models.SmallIntegerField()
#     penampilan_rate = models.SmallIntegerField()
#     kecepatan_rate = models.SmallIntegerField()
#     ketepatan_rate = models.SmallIntegerField()
#     informatif_rate = models.SmallIntegerField()
#     komentar_farmasi = models.TextField(blank=True, null=True)
#     komentar_farmasi_suara = models.FileField(upload_to='survey/voices/farmasi/',
#                                       null=True)

#     created_at = models.DateTimeField(
#         auto_now_add=True, blank=True, null=True)
#     deleted_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
#     class Meta:
#         managed = True
#         db_table = "survei_farmasi"
#         verbose_name = "Survei Farmasi"
#         verbose_name_plural = "Survei Farmasi"


# class SKMFasilitas(models.Model):
#     """Survei Kepuasan Masyarakat - Fasilitas

#     Args:
#         models (**kwargs): (
#             id_registrasi: Registrasi,
#             kelengkapan_rate: int,
#             kebersihan_rate: int,
#             kenyamanan_rate: int,
#             kamarmandi_rate: int,
#             kualitas_rate: int,
#             komentar: str(-1),
#             komentar_suara: FileField
#         )
#     """
#     id = models.AutoField(primary_key=True, db_column='id')
#     id_registrasi = models.ForeignKey(
#         Registrasi, models.DO_NOTHING, db_column="id_pendaftaran",
#         verbose_name="Nomor Registrasi")
#     kelengkapan_rate = models.SmallIntegerField()
#     kebersihan_rate = models.SmallIntegerField()
#     kenyamanan_rate = models.SmallIntegerField()
#     kamarmandi_rate = models.SmallIntegerField()
#     kualitas_rate = models.SmallIntegerField()
#     komentar_fasilitas = models.TextField(blank=True, null=True)
#     komentar_fasilitas_suara = models.FileField(upload_to='survey/voices/fasilitas/',
#                                       null=True)

#     created_at = models.DateTimeField(
#         auto_now_add=True, blank=True, null=True)
#     deleted_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
#     class Meta:
#         managed = True
#         db_table = "survei_fasilitas"
#         verbose_name = "Survei Fasilitas"
#         verbose_name_plural = "Survei Fasilitas"
    
    
    
