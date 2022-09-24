# Generated by Django 3.2 on 2022-09-23 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0007_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='phone_number',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='web_site',
            field=models.CharField(default='No web site', max_length=200),
        ),
    ]