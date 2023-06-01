from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Profile(models.Model):
    year = {
        ('2023','2023'),
        ('2024','2024'),
        ('2025','2025'),
        ('2026','2026')
    }

    sex={   
        ('male','Male'),
        ('female','Female'),
        ('others','Others')
    }

    programme = {
        ('B.TECH','Bachelor of Technology'),
        ('M.TECH','Master of Technology'),
        ('MCA','Master of Computer Applications'),
        ('MSc','Master of Science, Data Science'),
        ('OTH','others')
    }

    college = {
        ('NIT RRK','National Institute of Technology, Rourkela'),
        ('IIT BBSR', 'Indian Institute of Technology, Bhrbaneswar'),
        ('KIIT BBSR','Kalinga Institute of Industrial Technology, Bhubaneswar'),
        ('ITER BBSR', 'Institute of Technical Education and Research, Bhubaneswar'),
        ('CUTM BBSR','Centurion University of Technology and Management, Bhubaneswar'),
        ('CVRGU BBSR', 'C. V. Raman Global University, Bhubaneswar'),
        ('NIST BAM', 'National Institute of Science and Technology, Berhampur'),
        ('VSSUT SBP', 'Veer Surendra Sai University of Technology, Burla'),
        ('SOA BBSR', "Siksha 'O' Anusandhan University, Bhubaneswar"),
        ('BPUT BBSR','Biju Patnaik University of Technology, Rourkela'),
        ('SIT BBSR','Silicon Institute of Technology, Bhubaneswar'),
        ('CUTM PLH','Centurion University of Technology and Management, Paralkhemundi'),
        ('GIET GNPR','GIET University, Gunupur'),
        ('IIIT BBSR','International Institute of Information Technology, Bhubaneswar'),
        ('SSU CTC','Sri Sri University, Cuttack'),
        ('IGIT DNKL','Indira Gandhi Institute of Technology, Dhenkanal'),
        ('SIT SBP','Silicon Institute of Technology, Sambalpur'),
        ('XIM BBSR','XIM University, Bhubaneswar'),
        ('BEC BBSR','Bhubaneswar Engineering College, Bhubaneswar'),
        ('COEB BBSR','College of Engineering Bhubaneswar, Bhubaneswar'),
        ('CET','College of Engineering and Technology, Bhubaneswar'),
        ('GIFT','Gandhi Institute for Technology, Bhubaneswar'),
        ('OTH','others')
    }

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')
    
    # educational details
    institute=models.CharField(max_length=50, choices=college, blank=True)
    yop=models.CharField(max_length=4 , choices=year, default='2023')
    course=models.CharField(max_length=10, choices=programme, blank=True)
    skills = models.ManyToManyField(Skill)

    # personal details
    fullname=models.CharField(max_length=25, blank=True)
    gender=models.CharField(max_length=15, choices=sex, blank=True)
    city=models.CharField(default='Bhubaneswar', max_length=20)
    state=models.CharField(default='Odisha', max_length=20)  
    about=models.TextField(default='Hello there, I am using Integrated Coding')
    
    def __str__(self):
        return f'{self.user.username} Profile'

