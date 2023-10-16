# Generated by Django 4.2.6 on 2023-10-16 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customdoctor',
            name='heure',
        ),
        migrations.RemoveField(
            model_name='jour',
            name='docteurs',
        ),
        migrations.AddField(
            model_name='customdoctor',
            name='jours_disponibles',
            field=models.ManyToManyField(related_name='docteurs_disponibles', through='doctor.JourEtHeure', to='doctor.jour'),
        ),
    ]
