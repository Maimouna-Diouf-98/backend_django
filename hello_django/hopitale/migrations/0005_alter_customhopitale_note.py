# Generated by Django 4.2.6 on 2023-10-19 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hopitale', '0004_customhopitale_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customhopitale',
            name='note',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
