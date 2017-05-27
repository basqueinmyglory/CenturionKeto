from django.db import models

# Create your models here.

class Blogpost(models.Model):
    Fitness = 'Fitness'
    Diet = 'Diet'
    Creed = 'Creed'

    LABEL_OPTIONS = (
        (Fitness, 'Fitness'),
        (Diet, 'Diet'),
        (Creed, 'Creed'),
    )
    title = models.CharField(max_length=50, blank=True, null=True)
    pub_date = models.DateField(blank=True, null=True)
    author = models.CharField(max_length=25, blank=True, null=True)
    label = models.CharField(max_length=7, choices=LABEL_OPTIONS, default=Fitness)    
    content = models.TextField()


    def __str__(self):
        return str(self.pub_date) + " | " + str(self.title) 

    def summary(self):
        return self.content[:350]