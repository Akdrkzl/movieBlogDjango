# Generated by Django 4.2.7 on 2024-01-29 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0013_alter_cast_cast_role_alter_cast_gender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='video',
        ),
        migrations.AddField(
            model_name='movie',
            name='video_url',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
