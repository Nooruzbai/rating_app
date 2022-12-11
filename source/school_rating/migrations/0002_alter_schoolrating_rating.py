# Generated by Django 4.1.3 on 2022-12-11 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_rating', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolrating',
            name='rating',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_schools', to='school_rating.rating', verbose_name='School Rating'),
        ),
    ]
