# Generated by Django 5.0.1 on 2024-03-22 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textswap', '0004_apartment_washer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apartment',
            old_name='washer',
            new_name='washer_dryer',
        ),
    ]
