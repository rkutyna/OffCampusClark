# Generated by Django 5.0.1 on 2024-04-05 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textswap', '0014_alter_apartment_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='photo',
            field=models.ImageField(upload_to='static/images/'),
        ),
    ]
