# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-07 21:26
from __future__ import unicode_literals

import app_data.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields
import parler.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogAppConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100, verbose_name='Type')),
                ('namespace', models.CharField(default=None, max_length=100, unique=True, verbose_name='Instance namespace')),
                ('app_data', app_data.fields.AppDataField(default='{}', editable=False)),
            ],
            options={
                'verbose_name_plural': 'Apphook configs',
                'abstract': False,
                'verbose_name': 'Apphook config',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_published', models.BooleanField(default=False, verbose_name='Published')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'verbose_name_plural': 'Posts',
                'ordering': ['-created_at'],
                'verbose_name': 'Post',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PostTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('excerpt', models.CharField(blank=True, max_length=2000, verbose_name='Excerpt')),
                ('content', djangocms_text_ckeditor.fields.HTMLField(verbose_name='Content')),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='blog.Post')),
            ],
            options={
                'managed': True,
                'default_permissions': (),
                'db_tablespace': '',
                'db_table': 'blog_post_translation',
                'verbose_name': 'Post Translation',
            },
        ),
        migrations.AlterUniqueTogether(
            name='blogappconfig',
            unique_together=set([('type', 'namespace')]),
        ),
        migrations.AlterUniqueTogether(
            name='posttranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
