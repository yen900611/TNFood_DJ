# Generated by Django 3.2 on 2022-10-02 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0020_auto_20221002_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='devices',
            field=models.ManyToManyField(blank=True, to='food.Device'),
        ),
        migrations.AlterField(
            model_name='place',
            name='tag',
            field=models.ManyToManyField(blank=True, to='food.Tag'),
        ),
    ]
