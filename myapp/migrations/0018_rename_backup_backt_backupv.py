# Generated by Django 5.0.2 on 2024-02-15 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_backup_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='backt',
            old_name='backup',
            new_name='backupv',
        ),
    ]