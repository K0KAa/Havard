# Generated by Django 3.2.4 on 2021-06-08 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image_url',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
