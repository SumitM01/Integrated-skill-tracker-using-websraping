# Generated by Django 3.2.17 on 2023-04-19 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coding_profile', '0006_leaderboard_rank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaderboard',
            name='rank',
        ),
    ]
