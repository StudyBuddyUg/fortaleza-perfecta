# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LowerGrade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lower_grade_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ThemeCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=200)),
                ('right_answer', models.CharField(max_length=200)),
                ('answer', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ThemePack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('theme_name', models.CharField(max_length=200)),
                ('grade', models.ForeignKey(to='flashcards.LowerGrade')),
            ],
        ),
        migrations.CreateModel(
            name='TopicCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=200)),
                ('right_answer', models.CharField(max_length=200)),
                ('answer', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TopicPack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject_name', models.CharField(max_length=30)),
                ('topic_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UpperGrade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('upper_grade_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='topicpack',
            name='grade',
            field=models.ForeignKey(to='flashcards.UpperGrade'),
        ),
        migrations.AddField(
            model_name='topiccard',
            name='topic',
            field=models.ForeignKey(to='flashcards.TopicPack'),
        ),
        migrations.AddField(
            model_name='themecard',
            name='theme',
            field=models.ForeignKey(to='flashcards.ThemePack'),
        ),
    ]
