# Generated by Django 4.2 on 2023-04-10 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0002_rename_game_name_games_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Games',
        ),
    ]
