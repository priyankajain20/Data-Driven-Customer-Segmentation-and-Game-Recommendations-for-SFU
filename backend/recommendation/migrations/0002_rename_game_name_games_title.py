# Generated by Django 4.2 on 2023-04-10 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='games',
            old_name='game_name',
            new_name='Title',
        ),
    ]
