# Generated by Django 4.1.3 on 2023-07-21 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_rating', '0003_alter_commentlike_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='type',
        ),
    ]
