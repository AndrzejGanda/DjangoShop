# Generated by Django 3.2.4 on 2021-06-10 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0004_auto_20210610_2101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='kategoria',
            new_name='category',
        ),
    ]