# Generated by Django 2.0.4 on 2018-04-27 22:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0006_auto_20180424_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='date_add',
            field=models.DateField(default=datetime.datetime(2018, 4, 27, 22, 51, 42, 238770, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_join',
            field=models.DateField(default=datetime.datetime(2018, 4, 27, 22, 51, 42, 239771, tzinfo=utc)),
        ),
    ]