from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Country(models.Model):
    name = models.CharField('Страна', max_length=200)

    class Meta:
        db_table = 'countries'
        ordering = ['name']

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField('Локация', max_length=200)
    id_country = models.ForeignKey(Country, on_delete=models.CASCADE,
                                   verbose_name="Страна", db_column='id_country')

    class Meta:
        db_table = 'locations'
        ordering = ['name']

    def __str__(self):
        return self.name


class Travel(models.Model):
    name = models.CharField('Путешествие', max_length=200)
    id_loc = models.ForeignKey(Location, on_delete=models.CASCADE,
                               verbose_name="Локация", db_column='id_loc')
    num_likes = models.PositiveIntegerField('Кол-во лайков')
    path_time = models.PositiveIntegerField('Время в пути')
    distance = models.PositiveIntegerField('Дистанция, км')
    image_url = models.ImageField('Превью')
    id_owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                                 verbose_name="Владелец", db_column='id_owner')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'travels'
        ordering = ['-created_at']
        verbose_name = 'Путешествие'
        verbose_name_plural = 'Путешествия'

    def __str__(self):
        return self.name


class StepType(models.Model):
    name = models.CharField('Страна', max_length=200)
    color = models.CharField('Цвет HEX', max_length=6)

    class Meta:
        db_table = 'step_types'
        ordering = ['name']

    def __str__(self):
        return self.name


class HistoryType(models.Model):
    name = models.CharField('Страна', max_length=200)
    color = models.CharField('Цвет HEX', max_length=6)

    class Meta:
        db_table = 'history_types'
        ordering = ['name']

    def __str__(self):
        return self.name


class TravelStep(models.Model):
    id_travel = models.ForeignKey(Travel, on_delete=models.CASCADE,
                                  verbose_name="Путешествие", db_column='id_travel')
    ix_step = models.PositiveSmallIntegerField('Шаг')
    title = models.CharField('Заголовок', max_length=200)
    coords = ArrayField(models.FloatField(), verbose_name="Координаты", size=2)
    id_type = models.ForeignKey(StepType, on_delete=models.CASCADE,
                                verbose_name="Тип шага", db_column='id_type')

    class Meta:
        db_table = 'travel_steps'
        verbose_name = 'Шаг путешествия'
        verbose_name_plural = 'Шаги путешествия'
        unique_together = (('id_travel', 'ix_step'),)

    def __str__(self):
        return f"{self.id_travel} || {self.ix_step}:{self.title}"


class Tag(models.Model):
    name = models.CharField('Название', max_length=200)

    class Meta:
        db_table = 'tags'
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField('Модель', max_length=200)
    name = models.CharField('Название', max_length=200)
    image_url = models.ImageField('Превью')

    class Meta:
        db_table = 'cars'

    def __str__(self):
        return self.name


class CarIssue(models.Model):
    name = models.CharField('Название', max_length=200)
    icon_url = models.ImageField('Иконка')
    is_critical = models.BooleanField('Критически?')

    class Meta:
        db_table = 'car_issues'

    def __str__(self):
        return self.name


class LevelTag(models.Model):
    id_travel = models.ForeignKey(Travel, on_delete=models.CASCADE, verbose_name="Путешествие", db_column='id_travel')
    id_tag = models.ForeignKey(Tag, verbose_name='Тег', on_delete=models.CASCADE, db_column='id_tag')

    class Meta:
        db_table = 'travel_tags'
        verbose_name = 'Путешествие-Тег'
        verbose_name_plural = 'Путешествия-Теги'

    def __str__(self):
        return f"Travel: {self.id_travel} || tag: {self.id_tag}"


class UserTravel(models.Model):
    id_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                                verbose_name="Пользователь", db_column='id_user')
    id_travel = models.ForeignKey(Travel, on_delete=models.CASCADE,
                                  verbose_name="Путешествие", db_column='id_travel')
    start_datetime = models.DateTimeField('Время начала')
    end_datetime = models.DateTimeField('Время окончания', null=True)
    max_height = models.PositiveIntegerField('Покоренная высота')
    path_passed = models.PositiveBigIntegerField('Км позади')
    is_finished = models.BooleanField('Окончено?', default=False)

    class Meta:
        db_table = 'user_travels'
        verbose_name = 'Пользователь-Путешествие'
        verbose_name_plural = 'Пользователь-Путешествие'


class UserTravelStep(models.Model):
    id_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                                verbose_name="Пользователь", db_column='id_user')
    id_step = models.ForeignKey(TravelStep, on_delete=models.CASCADE,
                                verbose_name="Шаг путешествия", db_column='id_step')
    is_passed = models.BooleanField('Пройдено?', default=False)

    class Meta:
        db_table = 'user_travel_steps'
        verbose_name = 'Пользователь-Шаг путешествия'
        verbose_name_plural = 'Пользователь-Шаг путешествия'


class UserInsurance(models.Model):
    id_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                                verbose_name="Пользователь", db_column='id_user')
    doc_url = models.FileField('Файл')
    start_date = models.DateField('Время начала')
    end_date = models.DateField('Время окончания')

    class Meta:
        db_table = 'user_insurance'


class UserCar(models.Model):
    id_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                                verbose_name="Пользователь", db_column='id_user')
    id_car = models.ForeignKey(Car, on_delete=models.CASCADE,
                               verbose_name="Машина", db_column='id_car')
    id_insurance = models.ForeignKey(UserInsurance, on_delete=models.CASCADE,
                                     verbose_name="Страховка", db_column='id_insurance')
    issues = ArrayField(models.PositiveSmallIntegerField(), verbose_name="Проблемы")

    class Meta:
        db_table = 'user_cars'


class UserCarHistory(models.Model):
    id_user_car = models.ForeignKey(UserCar, on_delete=models.CASCADE,
                                    verbose_name="Машина пользователя", db_column='id_user_car')
    ix_history = models.PositiveSmallIntegerField('Шаг')
    title = models.CharField('Заголовок', max_length=200)
    date = models.DateField('Дата')
    id_type = models.ForeignKey(HistoryType, on_delete=models.CASCADE,
                                verbose_name="Тип шага", db_column='id_type')

    class Meta:
        db_table = 'user_car_histories'