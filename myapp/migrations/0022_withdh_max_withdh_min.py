# Generated by Django 5.0.2 on 2024-02-16 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_remove_depht_max_remove_depht_min_ucoin_max_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdh',
            name='max',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='withdh',
            name='min',
            field=models.IntegerField(default=10),
        ),
    ]
