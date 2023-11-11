from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_private = models.BooleanField(default=False)
    
    def __str__(self):
        return self.text
    

class Entry(models.Model):
    
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date_added = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'entries'
        
    def __str__(self):
        return f"{self.text[:50]}..."
    

class Comment(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.text