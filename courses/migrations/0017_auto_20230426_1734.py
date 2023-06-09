# Generated by Django 3.2.17 on 2023-04-26 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0016_alter_codingquestion_question_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codingquestion',
            name='question_difficulty',
            field=models.CharField(choices=[('Hard', 'Hard'), ('Easy', 'Easy'), ('Medium', 'Medium')], default='Easy', max_length=10),
        ),
        migrations.AlterField(
            model_name='codingquestion',
            name='question_type',
            field=models.CharField(choices=[('Trie', 'Trie'), ('Linkedlist', 'Linkedlist'), ('Heap', 'Heap'), ('Backtracking', 'Backtracking'), ('Stack & Queue', 'Stack & Queue'), ('Binary search tree', 'Binary Search Tree'), ('Greedy', 'Greedy'), ('Graph', 'Graph'), ('Array', 'Array '), ('Bit Maniputation', 'Bit Maniputaion'), ('Searching & Sorting', 'Searching & Sorting'), ('Binary tree', 'Binary Tree'), ('String', 'String'), ('Dynamic programming', 'Dynamic Programming'), ('Matrix', 'Matrix')], default='Array', max_length=30),
        ),
    ]
