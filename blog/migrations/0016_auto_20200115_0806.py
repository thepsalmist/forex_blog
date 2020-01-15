# Generated by Django 3.0.1 on 2020-01-15 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_post_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='next_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next', to='blog.Post'),
        ),
        migrations.AddField(
            model_name='post',
            name='previous_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previous', to='blog.Post'),
        ),
    ]
