from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-add_at')
        
    def popular(self):
        return self.order_by('-rating')
        
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(null=True)
    rating  = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name="q_to_likes")
    
    objects = QuestionManager()
    
    def __str__(self):
        return self.title
    
class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(null=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL, related_name="answer_to_question")
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="answer_to_user")
    
    def __str__(self):
        return self.text
    
