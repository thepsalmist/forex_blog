# Generated by Django 3.0.1 on 2020-01-01 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20191228_1544'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('publish',)},
        ),
    ]
