# Generated by Django 3.0 on 2020-02-05 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0013_articlepost_author_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlepost',
            name='author_img',
        ),
    ]