# Generated by Django 3.0.7 on 2020-06-24 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_api', '0002_auto_20200624_2325'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Decks',
            new_name='Deck',
        ),
    ]
