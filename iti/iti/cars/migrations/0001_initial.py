# Generated by Django 4.1.1 on 2022-09-27 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartype', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('carcolor', models.CharField(max_length=100)),
            ],
        ),
    ]
