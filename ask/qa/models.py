from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(null=true)
    rating  = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=true, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User)
    
    objects = QuestionManager()
    
    def __str__(self):
        return self.title
    
class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(null=true)
    question = models.ForeignKey(User, null=true, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, null=true, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.text
    
class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-add_at')
        
    def popular(self):
        return self.order_by('-rating')