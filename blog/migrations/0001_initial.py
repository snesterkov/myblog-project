# Generated by Django 3.1.7 on 2021-03-26 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=100)),
                ('blog_date', models.DateTimeField(auto_now_add=True)),
                ('blog_text', models.CharField(max_length=1000)),
                ('blog_image', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
