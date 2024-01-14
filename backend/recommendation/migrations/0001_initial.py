# Generated by Django 4.2 on 2023-04-10 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(default='', max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('game1', models.CharField(default='', max_length=200)),
                ('game2', models.CharField(default='', max_length=200)),
                ('game3', models.CharField(default='', max_length=200)),
                ('game4', models.CharField(default='', max_length=200)),
                ('game5', models.CharField(default='', max_length=200)),
            ],
        ),
    ]