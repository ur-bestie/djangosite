# Generated by Django 5.0.2 on 2024-03-27 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0037_charity_charitypayment_giftcardpay"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ucoin",
            name="max",
            field=models.IntegerField(default=9223372036854775807),
        ),
    ]
