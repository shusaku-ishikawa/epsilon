from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from datetime import datetime

from django.core.validators import (
    RegexValidator, MaxValueValidator, MinValueValidator
)

# Create your models here.
class UserManager(BaseUserManager):
    """ユーザーマネージャー."""
    
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """メールアドレスでの登録を必須にする"""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """is_staff(管理サイトにログインできるか)と、is_superuer(全ての権限)をFalseに"""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """スーパーユーザーは、is_staffとis_superuserをTrueに"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

category1s = [
    ('IT', 'IT'),
    ('ART', 'アート・デザイン'),
    ('CONTENTS', 'コンテンツ'),
    ('LIFE', 'ライフサポート'),
    ('OTHER', 'その他'),
]
category2s = [
    ("HP", "ホームページ作成"),
    ("SYSTEM", "システム製作"),
    ("PRINT", "印刷物デザイン"),
    ("GRAPHIC", "グラフィックデザイン"),
    ("ILLUST", "イラスト作成,撮影（写真）"),
    ("MOVIE", "撮影（映像）"),
    ("EDITING", "編集"),
    ("DTP", "DTP"),
    ("AUDIO", "音声収録"),
    ("EVNT-PLN", "イベント企画"),
    ("EVNT-SETUP", "イベント設営"),
    ("SALES", "営業支援"),
    ("SW", "ソフトウェア開発"),
    ("TRANSL", "翻訳・通訳"),
    ("CNSL", "コンサルティング"),
    ("WRT", "文章ライティング"),
    ("INTVW", "取材"),
    ("NW", "ネットワーク施工"),
    ("SVR", "サーバ関連"),
    ("LAW", "法務"),
    ("LABR", "労務"),
    ("ACCNT", "財務・会計"),
    ("GAME", "ゲーム製作"),
    ("MED", "医療"),
    ("CARE", "介護"),
    ('OTHER', 'その他'),
]
def get_years():
    this_year = datetime.today().year
    ys = []
    for i in range(100):
        y = str(this_year - i)
        ys.append((y, y))
    return ys

class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = '登録企業'
        verbose_name_plural = '登録企業'
    def __str__(self):
        return self.username
    email = models.EmailField(_('Email'), unique=True)
    company_name = models.CharField(
        verbose_name = '社名',
        max_length = 255
    )
    company_name_furigana = models.CharField(
        verbose_name = '会社名フリガナ',
        max_length = 255,
    )
    thumbnail = models.ImageField(
        verbose_name = 'サムネイル',
        null = True,
        blank = True,
        upload_to = 'thumbnail/'
    )
    category1 = models.CharField(
        verbose_name = '業種（大分類）',
        max_length = 100,
        choices = category1s
    )
    @property
    def category1_name(self):
        if not self.category1:
            return ''
        cat = [e for e in category1s if e[0] == self.category1]
        if len(cat) > 0:
            return cat[0][1]
        else:
            return ''
    category2 = models.CharField(
        verbose_name = '業種（小分類）',
        max_length = 100,
        choices=category2s
    )
    @property
    def category2_name(self):
        if not self.category2:
            return ''
        cat = [e for e in category2s if e[0] == self.category2]
        if len(cat) > 0:
            return cat[0][1]
        else:
            return ''

    short_description = models.TextField(
        verbose_name = '会社概要',
    )
    description = models.TextField(
        verbose_name = '業務内容説明',
    )
    phone = models.CharField(
        verbose_name = '電話番号',
        max_length = 100,
        validators = [
            RegexValidator(
                regex = '[0-9\-\+]+',
                message = 'フォーマットが不正です。'
            )
        ]
    )
    short_delivery = models.BooleanField(
        verbose_name = '短納期対応可',
        default = False
    )
    representative_name = models.CharField(
        verbose_name = '代表者名',
        max_length = 255,
        blank = True,
        default=""
    )
    established_at = models.CharField(
        verbose_name = '創業',
        max_length = 100,
        choices = get_years()
    )

    major_clients = models.TextField(
        verbose_name = '主な取引先',
        blank = True,
    )
    major_products = models.TextField(
        verbose_name = '主な製品',
        blank = True,
    )
    major_technologies = models.TextField(
        verbose_name = '主な技術',
        blank = True,
    )
    major_facilities = models.TextField(
        verbose_name = '主な施設',
        blank = True,
    )
    appeal_points = models.CharField(
        verbose_name = 'アピールポイント',
        blank = True,
        default="",
        max_length = 255,
    )
    poc_name = models.CharField(
        verbose_name = '担当者名',
        blank = True,
        default="",
        max_length = 100
    )
    website = models.URLField(
        blank = True,
        default="",
        verbose_name = 'website'
    )

    
    is_staff = models.BooleanField(
        _('管理者'),
        default=False,
        help_text=_(
        'Designates whether the user can log into this admin site.'),
    )
    is_superuser = models.BooleanField(
        _('スーパーユーザ'),
        default=False,
        help_text=_(
        'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('利用開始'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    @property
    def username(self):
        """username属性のゲッター
        他アプリケーションが、username属性にアクセスした場合に備えて定義
        メールアドレスを返す
        """
        return self.email
    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

