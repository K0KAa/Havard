# Generated by Django 3.2.4 on 2021-06-09 14:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_alter_listing_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]