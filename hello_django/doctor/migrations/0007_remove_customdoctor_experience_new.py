# Generated by Django 4.2.6 on 2023-10-17 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0006_alter_customdoctor_experience_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customdoctor',
            name='experience_new',
        ),
    ]
