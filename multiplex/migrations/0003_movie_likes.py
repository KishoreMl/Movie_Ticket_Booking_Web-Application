# Generated by Django 3.2 on 2021-10-16 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiplex', '0002_alter_movie_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]