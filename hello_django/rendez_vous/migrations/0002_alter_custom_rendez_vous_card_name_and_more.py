# Generated by Django 4.2.6 on 2023-10-23 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rendez_vous', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_rendez_vous',
            name='card_name',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='custom_rendez_vous',
            name='probleme',
            field=models.CharField(blank=True, null=True),
        ),
    ]
