# Generated by Django 3.0.1 on 2020-01-23 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20200121_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(choices=[('currency', 'CURRENCY'), ('banks', 'BANKS'), ('crypto', 'CRYPTO'), ('commodities', 'COMMODITIES'), ('education', 'EDUCATION'), ('analysis', 'ANALYSIS'), ('news', 'NEWS')], default='currency', max_length=100),
        ),
    ]