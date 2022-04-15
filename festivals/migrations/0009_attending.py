# Generated by Django 4.0.4 on 2022-04-15 12:29

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('festivals', '0008_hotel_website'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival_date', models.DateField()),
                ('depart_date', models.DateField()),
                ('price_range', models.FloatField(null=True)),
                ('activities', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), null=True, size=None)),
                ('comment', models.CharField(max_length=400)),
                ('festival', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attending', to='festivals.festival')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attending', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
