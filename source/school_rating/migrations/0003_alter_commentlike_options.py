# Generated by Django 4.1.3 on 2023-07-16 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_rating', '0002_alter_commentlike_options_alter_school_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentlike',
            options={'verbose_name': 'CommentLike', 'verbose_name_plural': 'CommentLikes'},
        ),
    ]