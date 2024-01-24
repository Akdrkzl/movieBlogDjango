# Generated by Django 4.2.7 on 2024-01-23 16:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0004_cast_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='language',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='release_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
