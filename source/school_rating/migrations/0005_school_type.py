# Generated by Django 4.1.3 on 2023-07-21 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_rating', '0004_remove_school_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='type',
            field=models.IntegerField(default=0, verbose_name='Type'),
        ),
    ]
