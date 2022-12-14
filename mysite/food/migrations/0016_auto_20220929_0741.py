# Generated by Django 3.2 on 2022-09-29 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0015_auto_20220928_0647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device_management',
            name='devices',
        ),
        migrations.RemoveField(
            model_name='device_management',
            name='place',
        ),
        migrations.RemoveField(
            model_name='place',
            name='devices',
        ),
        migrations.AddField(
            model_name='tag',
            name='style',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='tag_management',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='food.place'),
        ),
        migrations.AlterField(
            model_name='tag_management',
            name='tags',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='food.tag'),
        ),
        migrations.DeleteModel(
            name='Device',
        ),
        migrations.DeleteModel(
            name='Device_Management',
        ),
    ]
