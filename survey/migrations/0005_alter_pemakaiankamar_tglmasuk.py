# Generated by Django 3.2.5 on 2024-06-13 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_alter_pemakaiankamar_tglmasuk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pemakaiankamar',
            name='tglmasuk',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
