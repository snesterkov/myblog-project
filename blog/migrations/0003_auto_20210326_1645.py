# Generated by Django 3.1.7 on 2021-03-26 13:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210326_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
