# Generated by Django 3.0.7 on 2020-10-09 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_api', '0010_auto_20201008_1535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deck',
            old_name='hashtags',
            new_name='tags',
        ),
    ]