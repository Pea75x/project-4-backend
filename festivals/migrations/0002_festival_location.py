# Generated by Django 4.0.4 on 2022-04-14 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festivals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='festival',
            name='location',
            field=models.CharField(choices=[('All', 'All'), ('Croatia', 'Croatia'), ('Malta', 'Malta')], default='All', max_length=20),
        ),
    ]