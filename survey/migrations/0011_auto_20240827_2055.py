# Generated by Django 3.2.5 on 2024-08-27 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0010_surveikepuasanmasyarakatrev'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jenispegawai',
            name='nama',
            field=models.CharField(db_column='nama', max_length=20),
        ),
        migrations.AlterField(
            model_name='layanan',
            name='nama',
            field=models.CharField(db_column='nama', max_length=50),
        ),
        migrations.AlterField(
            model_name='pegawai',
            name='nama',
            field=models.CharField(db_column='nama', max_length=50),
        ),
    ]
