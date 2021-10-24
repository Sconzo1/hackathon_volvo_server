# Generated by Django 3.2.7 on 2021-10-24 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Уровень пользователя',
                'verbose_name_plural': 'Уровни пользователя',
                'db_table': 'user_levels',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип пользователя',
                'verbose_name_plural': 'Типы пользователя',
                'db_table': 'user_types',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Почта')),
                ('password', models.CharField(max_length=300, verbose_name='Пароль')),
                ('surname', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('birthdate', models.DateField(null=True, verbose_name='Дата рождения')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Модератор?')),
                ('last_login', models.DateTimeField(null=True, verbose_name='Время последнего входа')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('id_user_level', models.ForeignKey(db_column='id_user_level', on_delete=django.db.models.deletion.CASCADE, to='authentication.userlevel', verbose_name='Уровень пользователя')),
                ('id_user_type', models.ForeignKey(db_column='id_user_type', on_delete=django.db.models.deletion.CASCADE, to='authentication.usertype', verbose_name='Тип пользователя')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'db_table': 'users',
                'ordering': ['email'],
            },
        ),
    ]