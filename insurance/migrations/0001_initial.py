# Generated by Django 2.0.4 on 2018-04-27 23:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicle', '0008_auto_20180427_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_number', models.CharField(max_length=15)),
                ('date_apply', models.DateField(default=datetime.datetime(2018, 4, 27, 16, 13, 19, 463715))),
                ('date_add', models.DateField(auto_now_add=True, null=True)),
                ('type', models.CharField(choices=[('homenauto', 'Home & Auto Insurance'), ('auto', 'Auto Insurance'), ('personal', 'Personal Insurance'), ('farm', 'Farm Insurance'), ('life', 'Life Insurance'), ('health', 'Health Insurance'), ('techservice', 'Technology Services Insurance'), ('recreationalvehicle', 'Recreational Vehicle Insurance'), ('finacial', 'Financial Services')], default='personal', max_length=12)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('cancel', 'Cancel'), ('pending', 'Pending')], default='active', max_length=10)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insurance_policies', to='vehicle.Car')),
            ],
        ),
    ]
