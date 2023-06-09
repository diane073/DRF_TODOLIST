# Generated by Django 4.2 on 2023-04-27 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolists', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='title',
            new_name='content',
        ),
        migrations.AddField(
            model_name='todolist',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
