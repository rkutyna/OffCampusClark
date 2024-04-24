# Generated by Django 4.2.11 on 2024-04-24 13:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textswap', '0005_alter_photo_photo_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='num_baths',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='num_beds',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='num_sqr_ft',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='rent',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
