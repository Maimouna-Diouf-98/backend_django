# Generated by Django 4.2.6 on 2023-10-18 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hopitale', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customhopitale',
            name='activite',
        ),
    ]
