# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-02 19:15
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import readbooks.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('bio', models.CharField(max_length=256)),
                ('gender', models.CharField(choices=[(b'Male', b'Male'), (b'Female', b'Female'), (b'Other', b'Other')], max_length=6)),
                ('date_of_birth', models.DateField(default=datetime.date.today)),
                ('date_of_death', models.DateField(blank=True, null=True)),
                ('profile_picture', models.ImageField(blank=True, upload_to=readbooks.models.author_upload_directory)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('publication_date', models.DateField()),
                ('book_synopsis', models.CharField(max_length=256)),
                ('cover_picture', models.ImageField(blank=True, upload_to=readbooks.models.book_upload_directory)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('authors', models.ManyToManyField(to='readbooks.Author')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='BookRecommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='readbooks.Book')),
            ],
        ),
        migrations.CreateModel(
            name='BooksReadByUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('books', models.ManyToManyField(to='readbooks.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reader_comment', models.CharField(max_length=2000)),
                ('message_time', models.DateTimeField(auto_now=True)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='readbooks.Book')),
            ],
            options={
                'ordering': ['message_time'],
            },
        ),
        migrations.CreateModel(
            name='Critic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=256)),
                ('password', models.CharField(max_length=256)),
                ('favorite_quote', models.CharField(max_length=256)),
                ('gender', models.CharField(choices=[(b'Male', b'Male'), (b'Female', b'Female'), (b'Other', b'Other')], max_length=6)),
                ('date_of_birth', models.DateField(default=datetime.date.today)),
                ('profile_picture', models.ImageField(blank=True, upload_to=readbooks.models.critic_upload_directory)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('member_count', models.IntegerField(default=0)),
                ('group_description', models.CharField(max_length=256)),
                ('topic_count', models.IntegerField(default=0)),
                ('cover_picture', models.ImageField(blank=True, upload_to=readbooks.models.group_upload_directory)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_date', models.DateField(default=datetime.date.today)),
                ('member_status', models.CharField(choices=[(b'Moderator', b'Moderator'), (b'Admin', b'Admin'), (b'Member', b'Member')], max_length=9)),
                ('groups', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='readbooks.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=256)),
                ('website', models.URLField()),
                ('cover_picture', models.ImageField(blank=True, upload_to=readbooks.models.publisher_upload_directory)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=256)),
                ('password', models.CharField(max_length=256)),
                ('gender', models.CharField(choices=[(b'Male', b'Male'), (b'Female', b'Female'), (b'Other', b'Other')], max_length=6)),
                ('date_of_birth', models.DateField(default=datetime.date.today)),
                ('profile_picture', models.ImageField(blank=True, upload_to=readbooks.models.reader_upload_directory)),
                ('group_joined', models.ManyToManyField(through='readbooks.Membership', to='readbooks.Group')),
            ],
            options={
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='ReadersCurrentlyRead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_status_message', models.CharField(max_length=2000)),
                ('message_time', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='readbooks.Book')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='readbooks.Reader')),
            ],
            options={
                'ordering': ['message_time'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('review', models.CharField(max_length=3000)),
                ('status', models.CharField(choices=[(b'Draft', b'Draft'), (b'Published', b'Published')], max_length=9)),
                ('pubdate', models.DateField(blank=True, default=datetime.date.today)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='readbooks.Book')),
                ('critic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='readbooks.Critic')),
            ],
            options={
                'ordering': ['pubdate'],
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('topic_discussion', models.CharField(max_length=2000)),
                ('creation_date', models.DateField(default=datetime.date.today)),
                ('reply_count', models.IntegerField(default=0)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='readbooks.Reader')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='readbooks.Group')),
            ],
            options={
                'ordering': ['creation_date'],
            },
        ),
        migrations.CreateModel(
            name='TopicReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_reply', models.CharField(max_length=2000)),
                ('message_time', models.DateTimeField(auto_now=True)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='readbooks.Topic')),
                ('topic_reply_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='readbooks.Reader')),
            ],
            options={
                'ordering': ['message_time'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[(b'Reader', b'Reader'), (b'Critic', b'Critic')], max_length=6)),
                ('bio', models.CharField(max_length=256)),
                ('gender', models.CharField(choices=[(b'Male', b'Male'), (b'Female', b'Female'), (b'Other', b'Other')], max_length=6)),
                ('date_of_birth', models.DateField(blank=True)),
                ('profile_picture', models.ImageField(blank=True, upload_to=readbooks.models.user_upload_dir)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='membership',
            name='members',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='readbooks.Reader'),
        ),
        migrations.AddField(
            model_name='comment',
            name='reader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='readbooks.Reader'),
        ),
        migrations.AddField(
            model_name='booksreadbyusers',
            name='readers',
            field=models.ManyToManyField(to='readbooks.Reader'),
        ),
        migrations.AddField(
            model_name='bookrecommendation',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='readbooks.Group'),
        ),
        migrations.AddField(
            model_name='bookrecommendation',
            name='recommender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='readbooks.Reader'),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(to='readbooks.Genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='publishers',
            field=models.ManyToManyField(to='readbooks.Publisher'),
        ),
        migrations.AddField(
            model_name='book',
            name='reviews',
            field=models.ManyToManyField(through='readbooks.Review', to='readbooks.Critic'),
        ),
    ]