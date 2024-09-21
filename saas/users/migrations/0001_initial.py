# Generated by Django 5.1.1 on 2024-09-21 14:25

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.CharField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('first_name', models.CharField(help_text='User first name', max_length=50)),
                ('last_name', models.CharField(help_text='User last name', max_length=50)),
                ('email', models.EmailField(help_text='User email', max_length=254, unique=True)),
                ('hostel', models.CharField(choices=[('1', 'Prof. Saburi Biobaku Hall'), ('2', 'Prof. Eni Njoku Hall'), ('3', 'Baluba Kingdom'), ('4', 'King Jaja Hall')], help_text="User's hostel")),
                ('room_name', models.CharField(help_text="User's room name", max_length=30)),
                ('is_seller', models.BooleanField(default=False, help_text='Check if user is a seller')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
