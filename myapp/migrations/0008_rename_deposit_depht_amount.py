# Generated by Django 5.0.2 on 2024-02-15 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_depht_deposit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='depht',
            old_name='deposit',
            new_name='amount',
        ),
    ]
