# Generated by Django 3.0.1 on 2019-12-28 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comment_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
