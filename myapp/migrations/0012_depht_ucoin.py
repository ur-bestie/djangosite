# Generated by Django 5.0.2 on 2024-02-15 19:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_depht_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='depht',
            name='ucoin',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.ucoin'),
            preserve_default=False,
        ),
    ]
