# Generated by Django 4.1.7 on 2023-03-13 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamento', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='placa',
            field=models.CharField(max_length=8, null=True, unique=True),
        ),
    ]
