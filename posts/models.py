from django.db import models
from accounts.models import User

# Create your models here.

class Post(models.Model):
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=50)
    content = models.TextField()
    
    pub_date = models.DateTimeField(auto_now_add=True)
    

    
    