# Generated by Django 3.2 on 2022-10-14 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0025_alter_tag_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='value',
            field=models.CharField(default='None', max_length=30, unique=True),
        ),
    ]