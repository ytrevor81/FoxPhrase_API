# Generated by Django 3.0.7 on 2020-10-28 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_api', '0011_auto_20201009_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
