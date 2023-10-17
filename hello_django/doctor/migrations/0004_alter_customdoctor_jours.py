# Generated by Django 4.2.6 on 2023-10-16 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_remove_jouretheure_heure_remove_jouretheure_jours_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customdoctor',
            name='jours',
            field=models.CharField(choices=[('Lundi', 'Lundi'), ('Mardi', 'Mardi'), ('Mercredi', 'Mercredi'), ('Jeudi', 'Jeudi'), ('Vendredi', 'Vendredi'), ('Samedi', 'Samedi'), ('Dimanche', 'Dimanche')], default='lundi', max_length=10),
        ),
    ]
