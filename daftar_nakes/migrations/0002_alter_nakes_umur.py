# Generated by Django 3.2.7 on 2021-11-06 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daftar_nakes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nakes',
            name='umur',
            field=models.IntegerField(),
        ),
    ]
