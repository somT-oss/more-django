# Generated by Django 5.1.1 on 2024-09-22 10:38

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_community'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='id',
            field=models.CharField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
