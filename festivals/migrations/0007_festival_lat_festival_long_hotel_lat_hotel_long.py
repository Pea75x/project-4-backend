# Generated by Django 4.0.4 on 2022-04-15 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festivals', '0006_remove_festival_hotel_hotel_festival'),
    ]

    operations = [
        migrations.AddField(
            model_name='festival',
            name='lat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='festival',
            name='long',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='lat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='long',
            field=models.FloatField(null=True),
        ),
    ]
