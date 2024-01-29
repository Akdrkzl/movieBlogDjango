# Generated by Django 4.2.7 on 2024-01-23 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('birth', models.DateField()),
                ('location', models.CharField(max_length=50)),
                ('is_director', models.BooleanField(default=False)),
                ('is_writers', models.BooleanField(default=False)),
                ('is_actor', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('plot', models.TextField(max_length=100)),
                ('budget', models.CharField(max_length=15)),
                ('image', models.ImageField(upload_to='movie-pic')),
                ('video', models.FileField(upload_to='movie-video')),
            ],
        ),
    ]