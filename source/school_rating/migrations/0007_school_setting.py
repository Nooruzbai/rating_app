# Generated by Django 4.1.3 on 2023-07-21 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_rating', '0006_remove_school_setting'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='setting',
            field=models.IntegerField(default=0, verbose_name='Setting'),
        ),
    ]
