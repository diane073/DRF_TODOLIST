# Generated by Django 4.2 on 2023-04-27 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolists', '0002_rename_title_todolist_content_todolist_is_completed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='author',
            new_name='user',
        ),
    ]