# Generated by Django 5.0 on 2023-12-16 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_dnslog_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dnslog',
            name='location',
            field=models.CharField(blank='', default='', max_length=200),
        ),
    ]
