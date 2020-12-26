# Generated by Django 3.1.4 on 2020-12-25 13:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='category1',
            field=models.CharField(default='', max_length=100, verbose_name='業種（大分類）'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='category2',
            field=models.CharField(default='', max_length=100, verbose_name='業種（小分類）'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='company_name',
            field=models.CharField(default='aa', max_length=255, verbose_name='社名'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.TextField(default='a', verbose_name='業務内容説明'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default='', max_length=100, validators=[django.core.validators.RegexValidator(message='フォーマットが不正です。', regex='[0-9\\-\\+]+')], verbose_name='電話番号'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='short_delivery',
            field=models.BooleanField(default=False, verbose_name='短納期対応可'),
        ),
    ]
