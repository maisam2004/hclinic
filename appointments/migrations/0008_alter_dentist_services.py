# Generated by Django 5.0.6 on 2024-05-27 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0007_alter_appointment_service'),
        ('fee', '0002_alter_fee_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dentist',
            name='services',
            field=models.ManyToManyField(blank=True, related_name='dentists', to='fee.fee'),
        ),
    ]
