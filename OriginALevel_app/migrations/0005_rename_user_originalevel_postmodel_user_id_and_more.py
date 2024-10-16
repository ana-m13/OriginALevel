# Generated by Django 4.1 on 2023-02-04 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('OriginALevel_app', '0004_alter_originalevel_replymodel_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='originalevel_postmodel',
            old_name='user',
            new_name='user_id',
        ),
        migrations.RemoveField(
            model_name='originalevel_postmodel',
            name='rating',
        ),
        migrations.CreateModel(
            name='OriginALevel_RatingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_rating', models.IntegerField(blank=True, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_rating', to='OriginALevel_app.originalevel_postmodel')),
                ('rated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
