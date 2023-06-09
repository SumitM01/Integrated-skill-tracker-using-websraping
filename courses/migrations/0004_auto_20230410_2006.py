# Generated by Django 3.2.17 on 2023-04-10 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_delete_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestquestion',
            name='question_difficulty',
            field=models.CharField(choices=[('easy', 'Easy'), ('hard', 'Hard'), ('medium', 'Medium')], default='easy', max_length=10),
        ),
        migrations.AddField(
            model_name='contestquestion',
            name='question_type',
            field=models.CharField(choices=[('heap', 'Heap'), ('graph', 'Graph'), ('backtracking', 'Backtracking'), ('binary search tree', 'Binary Search Tree'), ('greedy', 'Greedy'), ('array', 'Array '), ('matrix', 'Matrix'), ('bit maniputation', 'Bit Maniputaion'), ('binary tree', 'Binary Tree'), ('stack & queue', 'Stack & Queue'), ('linkedlist', 'Linkedlist'), ('searching & sorting', 'Searching & Sorting'), ('string', 'String'), ('dynamic programming', 'Dynamic Programming')], default='array', max_length=30),
        ),
    ]
