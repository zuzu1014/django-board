from django.db import models
from accounts.models import User

# Create your models here.


class Post(models.Model):
    
    language_choices = [
    ("python", "python"),
    ("javascript", "javascript"),
    ("java", "java"),
    ("C++", "C++") 
    ]

    career_choices = [
        ("신입", "신입"),
        ("경력", "경력")
    ]
    
    location_choices = [
        ("경기도 성남시 분당구", "경기도 성남시 분당구"),
        ("서울특별시 강남구", "서울특별시 강남구"),
        ("서울특별시 서초구", "서울특별시 서초구"), 
        ("서울특별시 동작구", "서울특별시 동작구"), 
        ("제주특별자치도 서귀포구", "제주특별자치도 서귀포구"), 
        ("대전광역시 유성구", "대전광역시 유성구")
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    logo = models.ImageField(upload_to="posts/logo",null=True, blank=True)
    title = models.CharField(max_length=60)
    content = models.TextField()
    language = models.CharField(max_length=60,choices=language_choices)
    career = models.CharField(max_length=60, choices=career_choices)
    location = models.CharField(max_length=60, choices=location_choices)
    salary = models.CharField(max_length=60)
    deadline = models.DateField()


    pub_date = models.DateTimeField(auto_now_add=True)
    

    
    