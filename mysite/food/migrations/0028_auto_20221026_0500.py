# Generated by Django 3.2 on 2022-10-26 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0027_auto_20221026_0456'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, verbose_name='date published'),
        ),
    ]