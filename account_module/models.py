from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(upload_to='images/profile', verbose_name='تصویر آواتار', null=True, blank=True)
    about = models.TextField(blank=True, null=True)
    email_active_code = models.CharField(max_length=100, blank=True, null=True, verbose_name='کد فعالسازی ایمیل')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if not self.get_full_name() == '':
            return self.get_full_name()
        return self.username
