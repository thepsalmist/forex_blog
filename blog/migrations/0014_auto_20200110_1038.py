# Generated by Django 3.0.1 on 2020-01-10 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_contact'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-publish',)},
        ),
    ]