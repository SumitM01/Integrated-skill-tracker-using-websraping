# Generated by Django 3.2.17 on 2023-04-14 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0009_alter_contest_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contest',
            options={'ordering': ('date', 'time')},
        ),
    ]
