# Generated by Django 5.0.2 on 2024-02-13 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='media/%y')),
                ('address', models.CharField(max_length=100)),
                ('info', models.TextField(default='deposit information', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ucoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='media/%y')),
                ('address', models.CharField(max_length=100)),
                ('info', models.TextField(default='deposit information', max_length=100)),
            ],
        ),
    ]
