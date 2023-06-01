# Generated by Django 3.2.17 on 2023-04-03 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0003_alter_contest_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='status',
            field=models.CharField(choices=[('upcoming', 'Upcoming'), ('ongoing', 'Ongoing')], default='upcoming', max_length=10),
        ),
    ]