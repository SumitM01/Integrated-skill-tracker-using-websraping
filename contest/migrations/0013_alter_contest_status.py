# Generated by Django 3.2.17 on 2023-04-19 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0012_alter_contest_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='status',
            field=models.CharField(choices=[('expired', 'Expired'), ('upcoming', 'Upcoming'), ('ongoing', 'Ongoing')], default='upcoming', max_length=10),
        ),
    ]
