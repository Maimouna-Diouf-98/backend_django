# Generated by Django 4.2.6 on 2023-10-18 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jour_hopitale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jour', models.CharField(choices=[('Lundi', 'Lundi'), ('Mardi', 'Mardi'), ('Mercredi', 'Mercredi'), ('Jeudi', 'Jeudi'), ('Vendredi', 'Vendredi'), ('Samedi', 'Samedi'), ('Dimanche', 'Dimanche')], max_length=10)),
                ('heure_debut', models.TimeField(default='00:00:00')),
                ('heure_fin', models.TimeField(default='00:00:00')),
            ],
        ),
        migrations.CreateModel(
            name='CustomHopitale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('specialist', models.CharField(max_length=255)),
                ('activite', models.CharField(max_length=255)),
                ('adresse', models.CharField(blank=True, max_length=255, null=True)),
                ('about', models.CharField(blank=True, max_length=255, null=True)),
                ('heure', models.TimeField(default='00:00:00')),
                ('date', models.DateField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='hopital')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, editable=False, related_name='custom_hopital', to='auth.group')),
                ('jours', models.ManyToManyField(blank=True, related_name='hospitals', to='hopitale.jour_hopitale')),
                ('user_permissions', models.ManyToManyField(blank=True, editable=False, related_name='custom_hopital', to='auth.permission')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
