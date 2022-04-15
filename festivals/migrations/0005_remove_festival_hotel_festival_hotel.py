# Generated by Django 4.0.4 on 2022-04-15 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festivals', '0004_hotel_festival_hotel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='festival',
            name='hotel',
        ),
        migrations.AddField(
            model_name='festival',
            name='hotel',
            field=models.ManyToManyField(blank=True, related_name='festival', to='festivals.hotel'),
        ),
    ]
