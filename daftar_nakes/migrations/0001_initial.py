# Generated by Django 3.2.7 on 2021-11-06 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='nakes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=30)),
                ('umur', models.IntegerField(default=0)),
                ('rumah_sakit', models.CharField(max_length=30)),
                ('pendidikan', models.CharField(max_length=30)),
            ],
        ),
    ]
