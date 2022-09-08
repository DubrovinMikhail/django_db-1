# Generated by Django 4.1 on 2022-09-07 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0003_remove_phone_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='slug',
            field=models.SlugField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.URLField(max_length=250),
        ),
    ]
