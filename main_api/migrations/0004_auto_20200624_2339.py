# Generated by Django 3.0.7 on 2020-06-24 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_api', '0003_auto_20200624_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='comments',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='deck',
            name='likes',
            field=models.IntegerField(null=True),
        ),
    ]