# Generated by Django 3.2.5 on 2024-06-13 02:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_auto_20240613_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pemakaiankamar',
            name='tglmasuk',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
