# Generated by Django 4.1 on 2022-08-23 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vaccine',
            options={'ordering': ['name']},
        ),
    ]
