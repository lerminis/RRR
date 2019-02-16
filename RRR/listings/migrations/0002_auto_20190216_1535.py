# Generated by Django 2.1.7 on 2019-02-16 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnapprovedListing',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('listings.listing',),
        ),
        migrations.RemoveField(
            model_name='listing',
            name='is_hidden',
        ),
        migrations.AlterModelTable(
            name='listing',
            table='listings_listing',
        ),
    ]
