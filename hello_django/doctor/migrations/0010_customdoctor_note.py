# Generated by Django 4.2.6 on 2023-10-19 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0009_jour_doctor_remove_customdoctor_jours_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customdoctor',
            name='note',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=4, null=True),
        ),
    ]
