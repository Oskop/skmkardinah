# Generated by Django 3.2.5 on 2024-04-22 02:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instalasi',
            fields=[
                ('id', models.CharField(db_column='id', max_length=2, primary_key=True, serialize=False)),
                ('nama', models.CharField(db_column='nama', max_length=30)),
            ],
            options={
                'verbose_name': 'Instalasi',
                'verbose_name_plural': 'Instalasi-Instalasi',
                'db_table': 'instalasi',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Kamar',
            fields=[
                ('id', models.CharField(db_column='id', max_length=4, primary_key=True, serialize=False)),
                ('nama', models.CharField(db_column='nama', max_length=30)),
            ],
            options={
                'verbose_name': 'Kamar',
                'verbose_name_plural': 'Kamar-Kamar',
                'db_table': 'kamar',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Kecamatan',
            fields=[
                ('id', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('nama', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Kecamatan',
                'verbose_name_plural': 'Kecamatan',
                'db_table': 'kecamatan',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='KelasPelayanan',
            fields=[
                ('id', models.CharField(db_column='id', max_length=2, primary_key=True, serialize=False)),
                ('nama', models.CharField(db_column='nama', max_length=10)),
            ],
            options={
                'verbose_name': 'Kelas Pelayanan',
                'verbose_name_plural': 'Kelas-Kelas Pelayanan',
                'db_table': 'kelas_pelayanan',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Kelurahan',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nama', models.TextField(blank=True, null=True)),
                ('id_kecamatan', models.ForeignKey(blank=True, db_column='id_kecamatan', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='survey.kecamatan')),
            ],
            options={
                'verbose_name': 'Kelurahan',
                'verbose_name_plural': 'Kelurahan',
                'db_table': 'kelurahan',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Kotakab',
            fields=[
                ('id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('nama', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Kota Kabupaten',
                'verbose_name_plural': 'Kota Kabupaten',
                'db_table': 'kotakab',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pasien',
            fields=[
                ('nik', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('nocm', models.CharField(db_column='nocm', max_length=7, unique=True)),
                ('jk', models.CharField(blank=True, max_length=1, null=True)),
                ('tgl_lahir', models.DateTimeField(blank=True, null=True)),
                ('alamat', models.TextField(blank=True, null=True)),
                ('rt', models.CharField(blank=True, max_length=2, null=True)),
                ('rw', models.CharField(blank=True, max_length=2, null=True)),
                ('nama', models.CharField(blank=True, max_length=60, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('id_kelurahan', models.ForeignKey(blank=True, db_column='id_kelurahan', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='survey.kelurahan')),
                ('id_tmp_lahir', models.ForeignKey(blank=True, db_column='id_tmp_lahir', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='survey.kotakab')),
            ],
            options={
                'verbose_name': 'Pasien',
                'verbose_name_plural': 'Pasien-Pasien',
                'db_table': 'pasien',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Provinsi',
            fields=[
                ('id', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('nama', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Provinsi',
                'verbose_name_plural': 'Provinsi',
                'db_table': 'provinsi',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Registrasi',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('tglregistrasi', models.DateField(db_column='tglpendaftaran')),
                ('tglpulang', models.DateField(db_column='tglpulang')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('id_kelas', models.ForeignKey(db_column='id_kelas', on_delete=django.db.models.deletion.DO_NOTHING, to='survey.kelaspelayanan')),
                ('norm', models.ForeignKey(db_column='id_pasien', on_delete=django.db.models.deletion.DO_NOTHING, to='survey.pasien')),
            ],
            options={
                'verbose_name': 'Registrasi',
                'verbose_name_plural': 'Registrasi',
                'db_table': 'registrasi',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TempatTidur',
            fields=[
                ('id', models.CharField(db_column='id', max_length=4, primary_key=True, serialize=False)),
                ('nama', models.CharField(db_column='nama', max_length=10)),
                ('id_kamar', models.ForeignKey(db_column='id_kamar', on_delete=django.db.models.deletion.DO_NOTHING, to='survey.kamar')),
            ],
            options={
                'verbose_name': 'Tempat Tidur',
                'verbose_name_plural': 'Tempat-Tempat Tidur',
                'db_table': 'tempat_tidur',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SurveiKepuasanMasyarakat',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('fasilitas_rate', models.IntegerField()),
                ('perawat_rate', models.IntegerField()),
                ('dokter_rate', models.IntegerField()),
                ('farmasi_rate', models.IntegerField()),
                ('komentar', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('id_registrasi', models.ForeignKey(db_column='id_pendaftaran', on_delete=django.db.models.deletion.DO_NOTHING, to='survey.registrasi')),
            ],
            options={
                'verbose_name': 'Survei',
                'verbose_name_plural': 'Survei-Survei',
                'db_table': 'survei',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ruangan',
            fields=[
                ('id', models.CharField(db_column='id', max_length=3, primary_key=True, serialize=False)),
                ('nama', models.CharField(db_column='nama', max_length=30)),
                ('id_instalasi', models.ForeignKey(db_column='id_instalasi', on_delete=django.db.models.deletion.DO_NOTHING, to='survey.instalasi')),
            ],
            options={
                'verbose_name': 'Ruangan',
                'verbose_name_plural': 'Ruangan-Ruangan',
                'db_table': 'ruangan',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PemakaianKamar',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('tglmasuk', models.DateTimeField(default=datetime.datetime(2024, 4, 22, 9, 21, 16, 703841))),
                ('tglkeluar', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('id_registrasi', models.ForeignKey(db_column='id_pendaftaran', on_delete=django.db.models.deletion.DO_NOTHING, to='survey.registrasi')),
                ('id_tempattidur', models.ForeignKey(db_column='id_tempattidur', on_delete=django.db.models.deletion.DO_NOTHING, to='survey.tempattidur')),
            ],
            options={
                'verbose_name': 'Pemakaian Kamar',
                'verbose_name_plural': 'Riwayat Pemakaian Kamar',
                'db_table': 'pemakaian_kamar',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='kotakab',
            name='id_provinsi',
            field=models.ForeignKey(blank=True, db_column='id_provinsi', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='survey.provinsi'),
        ),
        migrations.AddField(
            model_name='kecamatan',
            name='id_kotakab',
            field=models.ForeignKey(blank=True, db_column='id_kotakab', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='survey.kotakab'),
        ),
        migrations.AddField(
            model_name='kamar',
            name='id_ruangan',
            field=models.ForeignKey(db_column='id_ruangan', on_delete=django.db.models.deletion.DO_NOTHING, to='survey.ruangan'),
        ),
    ]
