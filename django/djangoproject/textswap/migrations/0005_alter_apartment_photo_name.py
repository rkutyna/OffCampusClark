# Generated by Django 5.0.1 on 2024-04-05 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textswap', '0004_apartment_photo_name_alter_apartment_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='photo_name',
            field=models.CharField(default=None, max_length=100),
        ),
    ]