# Generated by Django 4.2 on 2023-04-27 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolists', '0003_rename_author_todolist_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='completed_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='todolist',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
