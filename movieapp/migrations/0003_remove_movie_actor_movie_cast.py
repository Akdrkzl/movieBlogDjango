# Generated by Django 4.2.7 on 2024-01-23 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_movie_actor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='actor',
        ),
        migrations.AddField(
            model_name='movie',
            name='cast',
            field=models.ManyToManyField(to='movieapp.cast'),
        ),
    ]
