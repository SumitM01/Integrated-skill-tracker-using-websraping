from django.db import models
from django.contrib.auth.models import User

class CodingQuestion(models.Model):

    difficulty = {
        ('Easy','Easy'),
        ('Medium','Medium'),
        ('Hard','Hard')
    }

    topic = {
        ('Array','Array '),
        ('Matrix','Matrix'),
        ('String','String'),
        ('Searching & Sorting','Searching & Sorting'),
        ('Linkedlist','Linkedlist'),
        ('Binary tree','Binary Tree'),
        ('Binary search tree','Binary Search Tree'),
        ('Greedy','Greedy'),
        ('Backtracking','Backtracking'),
        ('Stack & Queue','Stack & Queue'),
        ('Heap','Heap'),
        ('Graph','Graph'),
        ('Dynamic programming','Dynamic Programming'),
        ('Bit Maniputation','Bit Maniputaion'),
        ('Trie','Trie')
    }

    question_no = models.AutoField(primary_key=True)
    question_name = models.CharField(max_length=1000)
    question_link = models.CharField(max_length=10000)
    question_difficulty = models.CharField(max_length=10, choices=difficulty, default='Easy')
    question_type = models.CharField(max_length=30, choices=topic, default='Array')
    
    def __str__(self):
        return self.question_name
 

class UserCodingQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(CodingQuestion, on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'question')

    def __str__(self):
        return f"{self.user.username} - {self.question.question_name}"
 