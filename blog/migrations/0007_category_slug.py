# Generated by Django 3.0.1 on 2019-12-27 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='default', max_length=200),
            preserve_default=False,
        ),
    ]