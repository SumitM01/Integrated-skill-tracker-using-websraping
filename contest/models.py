from django.db import models

class Platform(models.Model):
    name= models.CharField(max_length=50)
    image=models.ImageField(default='default.jpg',upload_to='contest_logo')

    def __str__(self):
        return self.name

class Contest(models.Model):

    class ContestObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status = 'upcoming')

    options = {
        ('upcoming', 'Upcoming'),
        ('ongoing', 'Ongoing'),
        ('expired', 'Expired'),
        ('constant', 'Constant')
    }

    platform = models.ForeignKey(Platform, on_delete=models.PROTECT, default='platform')
    name = models.CharField(max_length=100, unique=True)
    date = models.DateField()
    time = models.TimeField()
    end_time = models.DateTimeField(null=True)
    duration = models.CharField(max_length=50,null=True)
    status = models.CharField(max_length=10, choices=options, default='upcoming')
    link =models.CharField(max_length=100,null=True)
    objects = models.Manager()  # default manager
    contestobjects = ContestObjects()  # custom manager

    class Meta:
        ordering = ('date','time')

    def __str__(self):
        return self.name

