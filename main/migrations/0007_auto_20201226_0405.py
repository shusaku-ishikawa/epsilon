# Generated by Django 3.1.4 on 2020-12-26 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20201226_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='short_description',
            field=models.TextField(verbose_name='会社概要'),
        ),
    ]
