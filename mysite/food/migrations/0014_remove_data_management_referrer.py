# Generated by Django 3.2 on 2022-09-28 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0013_auto_20220928_0541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data_management',
            name='referrer',
        ),
    ]
