# Generated by Django 4.2.6 on 2023-10-25 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rendez_vous', '0021_alter_customrendezvous_card_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('card_number', models.IntegerField(blank=True, default=0, null=True)),
                ('expiry_date', models.DateField(blank=True, default='', null=True)),
                ('cvv', models.IntegerField(blank=True, default=0, null=True)),
                ('save_to_database', models.BooleanField(blank=True, default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='customrendezvous',
            name='card_name',
        ),
        migrations.RemoveField(
            model_name='customrendezvous',
            name='card_number',
        ),
        migrations.RemoveField(
            model_name='customrendezvous',
            name='cvv',
        ),
        migrations.RemoveField(
            model_name='customrendezvous',
            name='expiry_date',
        ),
        migrations.RemoveField(
            model_name='customrendezvous',
            name='save_to_database',
        ),
    ]
