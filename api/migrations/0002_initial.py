# Generated by Django 3.2.7 on 2021-10-24 07:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='usertravelstep',
            name='id_user',
            field=models.ForeignKey(db_column='id_user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='usertravel',
            name='id_travel',
            field=models.ForeignKey(db_column='id_travel', on_delete=django.db.models.deletion.CASCADE, to='api.travel', verbose_name='Путешествие'),
        ),
        migrations.AddField(
            model_name='usertravel',
            name='id_user',
            field=models.ForeignKey(db_column='id_user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='userinsurance',
            name='id_user',
            field=models.ForeignKey(db_column='id_user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='usercarhistory',
            name='id_type',
            field=models.ForeignKey(db_column='id_type', on_delete=django.db.models.deletion.CASCADE, to='api.historytype', verbose_name='Тип шага'),
        ),
        migrations.AddField(
            model_name='usercarhistory',
            name='id_user_car',
            field=models.ForeignKey(db_column='id_user_car', on_delete=django.db.models.deletion.CASCADE, to='api.usercar', verbose_name='Машина пользователя'),
        ),
        migrations.AddField(
            model_name='usercar',
            name='id_car',
            field=models.ForeignKey(db_column='id_car', on_delete=django.db.models.deletion.CASCADE, to='api.car', verbose_name='Машина'),
        ),
        migrations.AddField(
            model_name='usercar',
            name='id_insurance',
            field=models.ForeignKey(db_column='id_insurance', on_delete=django.db.models.deletion.CASCADE, to='api.userinsurance', verbose_name='Страховка'),
        ),
        migrations.AddField(
            model_name='usercar',
            name='id_user',
            field=models.ForeignKey(db_column='id_user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='travelstep',
            name='id_travel',
            field=models.ForeignKey(db_column='id_travel', on_delete=django.db.models.deletion.CASCADE, to='api.travel', verbose_name='Путешествие'),
        ),
        migrations.AddField(
            model_name='travelstep',
            name='id_type',
            field=models.ForeignKey(db_column='id_type', on_delete=django.db.models.deletion.CASCADE, to='api.steptype', verbose_name='Тип шага'),
        ),
        migrations.AddField(
            model_name='travel',
            name='id_loc',
            field=models.ForeignKey(db_column='id_loc', on_delete=django.db.models.deletion.CASCADE, to='api.location', verbose_name='Локация'),
        ),
        migrations.AddField(
            model_name='travel',
            name='id_owner',
            field=models.ForeignKey(db_column='id_owner', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
        migrations.AddField(
            model_name='location',
            name='id_country',
            field=models.ForeignKey(db_column='id_country', on_delete=django.db.models.deletion.CASCADE, to='api.country', verbose_name='Страна'),
        ),
        migrations.AddField(
            model_name='leveltag',
            name='id_tag',
            field=models.ForeignKey(db_column='id_tag', on_delete=django.db.models.deletion.CASCADE, to='api.tag', verbose_name='Тег'),
        ),
        migrations.AddField(
            model_name='leveltag',
            name='id_travel',
            field=models.ForeignKey(db_column='id_travel', on_delete=django.db.models.deletion.CASCADE, to='api.travel', verbose_name='Путешествие'),
        ),
        migrations.AlterUniqueTogether(
            name='travelstep',
            unique_together={('id_travel', 'ix_step')},
        ),
    ]
