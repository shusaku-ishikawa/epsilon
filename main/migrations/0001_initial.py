# Generated by Django 3.1.4 on 2020-12-26 08:28

import django.core.validators
from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('company_name', models.CharField(max_length=255, verbose_name='社名')),
                ('company_name_furigana', models.CharField(max_length=255, verbose_name='会社名フリガナ')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='thumbnail/', verbose_name='サムネイル')),
                ('category1', models.CharField(max_length=100, verbose_name='業種（大分類）')),
                ('category2', models.CharField(max_length=100, verbose_name='業種（小分類）')),
                ('short_description', models.TextField(verbose_name='会社概要')),
                ('description', models.TextField(verbose_name='業務内容説明')),
                ('phone', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='フォーマットが不正です。', regex='[0-9\\-\\+]+')], verbose_name='電話番号')),
                ('short_delivery', models.BooleanField(default=False, verbose_name='短納期対応可')),
                ('representative_name', models.CharField(blank=True, default='', max_length=255, verbose_name='代表者名')),
                ('established_at', models.CharField(choices=[('1900', '1900')], max_length=100, verbose_name='創業')),
                ('major_clients', models.TextField(blank=True, verbose_name='主な取引先')),
                ('major_products', models.TextField(blank=True, verbose_name='主な製品')),
                ('major_technologies', models.TextField(blank=True, verbose_name='主な技術')),
                ('major_facilities', models.TextField(blank=True, verbose_name='主な施設')),
                ('appeal_points', models.CharField(blank=True, default='', max_length=255, verbose_name='アピールポイント')),
                ('poc_name', models.CharField(blank=True, default='', max_length=100, verbose_name='担当者名')),
                ('website', models.URLField(blank=True, default='', verbose_name='website')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='管理者')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='スーパーユーザ')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='利用開始')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', main.models.UserManager()),
            ],
        ),
    ]
