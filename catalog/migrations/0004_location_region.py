# Generated by Django 2.0.3 on 2018-03-19 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20180319_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='region',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
