# Generated by Django 5.0.6 on 2024-06-06 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textswap', '0006_alter_apartment_num_baths_alter_apartment_num_beds_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='user2_id',
            new_name='receiver',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='user1_id',
            new_name='sender',
        ),
        migrations.AddField(
            model_name='message',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]
