# Generated by Django 5.0.2 on 2024-02-13 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sitename', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='signininfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(default='header', max_length=30)),
                ('info', models.CharField(default='info', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='signupinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(default='header', max_length=30)),
                ('info', models.CharField(default='info', max_length=30)),
            ],
        ),
    ]
