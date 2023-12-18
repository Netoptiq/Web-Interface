# Generated by Django 5.0 on 2023-12-18 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_delete_delay_delete_domaincount_remove_log_query_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dnslog',
            old_name='location',
            new_name='latitude',
        ),
        migrations.AddField(
            model_name='dnslog',
            name='longitude',
            field=models.CharField(blank='', default='', max_length=200),
        ),
    ]