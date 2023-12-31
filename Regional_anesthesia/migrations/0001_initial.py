# Generated by Django 4.2.5 on 2023-09-14 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modul',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название Общеобразовательного модуля')),
                ('is_active', models.BooleanField(default=True, verbose_name='активный')),
            ],
            options={
                'verbose_name': 'Добавить Модуль',
                'verbose_name_plural': 'Модули',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbers', models.PositiveSmallIntegerField(verbose_name='Порядковый номер')),
                ('lessonNo', models.CharField(choices=[('LESSON ONE', 'Занятие 1.'), ('LESSON TWO', 'Занятие 2.'), ('LESSON THREE', 'Занятие 3.'), ('LESSON FOUR', 'Занятие 4.'), ('LESSON FIVE', 'Занятие 5.')], verbose_name='Занятие')),
                ('lesson', models.CharField(max_length=200, verbose_name='Название занятия')),
                ('subject', models.CharField(max_length=200, verbose_name='Тема')),
                ('description', models.TextField(verbose_name='Описание')),
                ('form', models.CharField(blank=True, choices=[('FORM ONE', 'Обзорная лекция.'), ('FORM TWO', 'Лекция.'), ('FORM THREE', 'Практикум.'), ('FORM FOUR', 'Консультация.'), ('FORM FIVE', 'Беседа.'), ('FORM SIX', 'Круглый стол.')], max_length=20, null=True, verbose_name='Форма проведения')),
                ('hour', models.CharField(blank=True, choices=[('HOUR ONE', '1 час.'), ('HOUR TWO', '2 часа.'), ('HOUR THREE', '3 часа.'), ('HOUR FOUR', '4 часа.')], max_length=20, null=True, verbose_name='Количество часов')),
                ('image', models.ImageField(blank=True, null=True, upload_to='lesson/', verbose_name='Изображение')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Regional_anesthesia.modul', verbose_name='Название общего курса')),
            ],
            options={
                'verbose_name': 'Добавить занятие',
                'verbose_name_plural': 'Занятия',
                'ordering': ('lesson',),
            },
        ),
    ]
