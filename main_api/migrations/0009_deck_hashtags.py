# Generated by Django 3.0.7 on 2020-10-06 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_api', '0008_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='hashtags',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
