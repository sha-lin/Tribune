# Generated by Django 3.2.7 on 2021-10-07 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_article_article_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='editor',
            options={'ordering': ['first_name']},
        ),
    ]
