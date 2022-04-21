# Generated by Django 4.0.4 on 2022-04-21 10:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('festivals', '0017_remove_message_destination_user_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
