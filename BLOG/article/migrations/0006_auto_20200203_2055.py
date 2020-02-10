# Generated by Django 3.0 on 2020-02-03 12:55

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20200203_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='title_img',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='article_title_img/%Y%m%d/', verbose_name='标题图片'),
        ),
    ]