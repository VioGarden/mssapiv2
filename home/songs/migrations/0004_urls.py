# Generated by Django 4.1.4 on 2022-12-12 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0003_songs_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, max_length=120)),
                ('edit_url', models.URLField(blank=True, max_length=120)),
                ('delete_url', models.URLField(blank=True, max_length=120)),
            ],
        ),
    ]
