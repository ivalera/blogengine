# Generated by Django 3.1.5 on 2021-01-12 09:46

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210112_1243'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='tag',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
