# Generated by Django 4.2.1 on 2023-10-10 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glue', '0002_rename_todo_todo_todo_list_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='add_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
