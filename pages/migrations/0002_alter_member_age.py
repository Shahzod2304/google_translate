# Generated by Django 4.0.4 on 2022-04-19 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.PositiveIntegerField(max_length=2),
        ),
    ]
