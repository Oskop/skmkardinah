# Generated by Django 3.2.5 on 2024-09-05 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0011_auto_20240827_2055'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pegawai',
            options={'managed': True, 'verbose_name': 'Pegawai', 'verbose_name_plural': 'Direktur'},
        ),
        migrations.AddField(
            model_name='pegawai',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
