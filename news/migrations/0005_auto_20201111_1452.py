# Generated by Django 3.1.3 on 2020-11-11 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_article_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(blank=True, null=True, upload_to='articles/'),
        ),
    ]
