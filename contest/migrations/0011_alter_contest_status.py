# Generated by Django 3.2.17 on 2023-04-19 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0010_alter_contest_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='status',
            field=models.CharField(choices=[('upcoming', 'Upcoming'), ('expired', 'Expired'), ('ongoing', 'Ongoing')], default='upcoming', max_length=10),
        ),
    ]
