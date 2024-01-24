# Generated by Django 4.2.7 on 2024-01-24 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0006_movie_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cast_Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='cast',
            name='is_actor',
        ),
        migrations.RemoveField(
            model_name='cast',
            name='is_director',
        ),
        migrations.RemoveField(
            model_name='cast',
            name='is_writers',
        ),
    ]
