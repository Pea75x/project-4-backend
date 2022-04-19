# Generated by Django 4.0.4 on 2022-04-19 09:47

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('festivals', '0010_rename_price_range_attending_price_max_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupTrip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pending_members', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), null=True, size=None)),
                ('members', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), null=True, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destinationUserId', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=500)),
                ('sourceUserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
