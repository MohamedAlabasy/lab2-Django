# Generated by Django 4.0.4 on 2022-04-21 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='details',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='image',
            field=models.URLField(null=True),
        ),
    ]
