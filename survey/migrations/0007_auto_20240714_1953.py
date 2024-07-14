# Generated by Django 3.2.5 on 2024-07-14 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_alter_registrasi_norm'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveikepuasanmasyarakat',
            name='komentar_suara',
            field=models.FileField(null=True, upload_to='survey/voices/'),
        ),
        migrations.AlterField(
            model_name='kamar',
            name='id_ruangan',
            field=models.ForeignKey(db_column='id_ruangan', on_delete=django.db.models.deletion.DO_NOTHING, to='survey.ruangan', verbose_name='Ruangan'),
        ),
        migrations.AlterField(
            model_name='pasien',
            name='id_kelurahan',
            field=models.ForeignKey(blank=True, db_column='id_kelurahan', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='survey.kelurahan', verbose_name='Kelurahan'),
        ),
        migrations.AlterField(
            model_name='pasien',
            name='id_tmp_lahir',
            field=models.ForeignKey(blank=True, db_column='id_tmp_lahir', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='survey.kotakab', verbose_name='Tempat Lahir'),
        ),
        migrations.AlterField(
            model_name='pasien',
            name='tgl_lahir',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Tanggal Lahir'),
        ),
        migrations.AlterField(
            model_name='pemakaiankamar',
            name='id_registrasi',
            field=models.ForeignKey(db_column='id_pendaftaran', on_delete=django.db.models.deletion.DO_NOTHING, to='survey.registrasi', verbose_name='Nomor Registrasi'),
        ),
        migrations.AlterField(
            model_name='pemakaiankamar',
            name='id_tempattidur',
            field=models.ForeignKey(db_column='id_tempattidur', on_delete=django.db.models.deletion.DO_NOTHING, to='survey.tempattidur', verbose_name='Tempat Tidur'),
        ),
        migrations.AlterField(
            model_name='pemakaiankamar',
            name='tglkeluar',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Tanggal Keluar'),
        ),
        migrations.AlterField(
            model_name='pemakaiankamar',
            name='tglmasuk',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Tanggal Masuk'),
        ),
        migrations.AlterField(
            model_name='registrasi',
            name='id_kelas',
            field=models.ForeignKey(db_column='id_kelas', on_delete=django.db.models.deletion.DO_NOTHING, to='survey.kelaspelayanan', verbose_name='Kelas Pelayanan'),
        ),
        migrations.AlterField(
            model_name='registrasi',
            name='norm',
            field=models.ForeignKey(db_column='id_pasien', on_delete=django.db.models.deletion.DO_NOTHING, to='survey.pasien', to_field='nocm', verbose_name='Pasien'),
        ),
        migrations.AlterField(
            model_name='registrasi',
            name='tglpulang',
            field=models.DateTimeField(blank=True, db_column='tglpulang', null=True, verbose_name='Tanggal Pulang'),
        ),
        migrations.AlterField(
            model_name='registrasi',
            name='tglregistrasi',
            field=models.DateTimeField(db_column='tglpendaftaran', verbose_name='Tanggal Registrasi'),
        ),
        migrations.AlterField(
            model_name='ruangan',
            name='id_instalasi',
            field=models.ForeignKey(db_column='id_instalasi', on_delete=django.db.models.deletion.DO_NOTHING, to='survey.instalasi', verbose_name='Instalasi'),
        ),
        migrations.AlterField(
            model_name='surveikepuasanmasyarakat',
            name='id_registrasi',
            field=models.ForeignKey(db_column='id_pendaftaran', on_delete=django.db.models.deletion.DO_NOTHING, to='survey.registrasi', verbose_name='Nomor Registrasi'),
        ),
        migrations.AlterField(
            model_name='tempattidur',
            name='id_kamar',
            field=models.ForeignKey(db_column='id_kamar', on_delete=django.db.models.deletion.DO_NOTHING, to='survey.kamar', verbose_name='Kamar'),
        ),
    ]
