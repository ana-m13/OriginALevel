# Generated by Django 4.1 on 2023-02-04 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OriginALevel_app', '0006_rename__rating_originalevel_ratingmodel_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='originalevel_ratingmodel',
            name='rating',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]