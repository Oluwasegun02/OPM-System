from django.db import models

# Create your models here.
class Portfolio(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Project(models.Model):
    portfolio = models.ForeignKey(Portfolio, related_name='projects', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    
