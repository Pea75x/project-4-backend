# Generated by Django 4.0.4 on 2022-04-20 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('festivals', '0015_delete_attending'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='destinationUserId',
            new_name='destination_user_id',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='sourceUserId',
            new_name='source_user_id',
        ),
    ]
