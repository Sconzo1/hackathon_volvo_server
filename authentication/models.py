from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from authentication.managers import UserManager


class UserType(models.Model):
    name = models.CharField('Название', max_length=200)

    class Meta:
        db_table = 'user_types'
        ordering = ['name']
        verbose_name = 'Тип пользователя'
        verbose_name_plural = 'Типы пользователя'

    def __str__(self):
        return self.name


class UserLevel(models.Model):
    name = models.CharField('Название', max_length=200)

    class Meta:
        db_table = 'user_levels'
        ordering = ['name']
        verbose_name = 'Уровень пользователя'
        verbose_name_plural = 'Уровни пользователя'

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Почта', unique=True, max_length=100)
    password = models.CharField('Пароль', max_length=300)

    surname = models.CharField('Фамилия', max_length=150)
    name = models.CharField('Имя', max_length=150)
    birthdate = models.DateField('Дата рождения', null=True)
    id_user_type = models.ForeignKey(UserType, models.CASCADE, verbose_name='Тип пользователя',
                                     db_column='id_user_type')
    id_user_level = models.ForeignKey(UserLevel, models.CASCADE, verbose_name='Уровень пользователя',
                                      db_column='id_user_level')

    is_staff = models.BooleanField('Модератор?', default=False)
    last_login = models.DateTimeField('Время последнего входа', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = 'users'
        ordering = ['email']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.surname}, {self.name}"
