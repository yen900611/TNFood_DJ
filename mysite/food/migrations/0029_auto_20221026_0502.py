# Generated by Django 3.2 on 2022-10-26 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0028_auto_20221026_0500'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]