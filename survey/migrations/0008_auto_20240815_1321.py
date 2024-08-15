# Generated by Django 3.2.5 on 2024-08-15 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0007_auto_20240714_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='JenisPegawai',
            fields=[
                ('id', models.CharField(db_column='id', max_length=2, primary_key=True, serialize=False)),
                ('nama', models.CharField(db_column='nama', max_length=10)),
            ],
            options={
                'verbose_name': 'Jenis Pegawai',
                'verbose_name_plural': 'Jenis-Jenis Pegawai',
                'db_table': 'jenis_pegawai',
                'managed': True,
            },
        ),
        migrations.AlterField(
            model_name='kecamatan',
            name='id_kotakab',
            field=models.ForeignKey(blank=True, db_column='id_kotakab', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='survey.kotakab', verbose_name='Kota/Kabupaten'),
        ),
        migrations.AlterField(
            model_name='kelurahan',
            name='id_kecamatan',
            field=models.ForeignKey(blank=True, db_column='id_kecamatan', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='survey.kecamatan', verbose_name='Kecamatan'),
        ),
        migrations.AlterField(
            model_name='kotakab',
            name='id_provinsi',
            field=models.ForeignKey(blank=True, db_column='id_provinsi', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='survey.provinsi', verbose_name='Provinsi'),
        ),
        migrations.CreateModel(
            name='Pelayanan',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('tglmasuk', models.DateTimeField(auto_now_add=True, verbose_name='Tanggal Masuk')),
                ('tglkeluar', models.DateTimeField(blank=True, null=True, verbose_name='Tanggal Keluar')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('id_registrasi', models.ForeignKey(db_column='id_pendaftaran', on_delete=django.db.models.deletion.DO_NOTHING, to='survey.registrasi', verbose_name='Nomor Registrasi')),
                ('id_tempattidur', models.ForeignKey(db_column='id_tempattidur', on_delete=django.db.models.deletion.DO_NOTHING, to='survey.tempattidur', verbose_name='Tempat Tidur')),
            ],
            options={
                'verbose_name': 'Pelayanan',
                'verbose_name_plural': 'Pelayanan',
                'db_table': 'pelayanan',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pegawai',
            fields=[
                ('id', models.CharField(db_column='id', max_length=10, primary_key=True, serialize=False)),
                ('nama', models.CharField(db_column='nama', max_length=10)),
                ('jenis_pegawai', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='survey.jenispegawai', verbose_name='Jenis Pegawai')),
            ],
            options={
                'verbose_name': 'Pegawai',
                'verbose_name_plural': 'Para Pegawai',
                'db_table': 'pegawai',
                'managed': True,
            },
        ),
    ]
