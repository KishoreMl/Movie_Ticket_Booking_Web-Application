# Generated by Django 3.2 on 2021-10-19 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiplex', '0009_auto_20211019_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='cast',
            name='image',
            field=models.ImageField(default=0, upload_to='Images/cast'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crew',
            name='image',
            field=models.ImageField(default=0, upload_to='Images/cast'),
            preserve_default=False,
        ),
    ]