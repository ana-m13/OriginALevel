# Generated by Django 4.1 on 2023-01-10 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OriginALevel_app', '0002_originalevel_postmodel_tag_code_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='originalevel_replymodel',
            old_name='user',
            new_name='replied_by',
        ),
    ]
