from django.core.management.base import BaseCommand, CommandError
from posts.models import Post
from accounts.models import User

import random
from random import randint
import datetime

campany_list = ["퓨처 컴퍼니", "투게더 컴퍼니", "하와이 컴퍼니", "서울 컴퍼니", "라이트 컴퍼니"]
salary_list = ["3500 ~ 3700 만원", "4200 ~ 4300 만원", "2200 ~ 2500 만원", "3500 ~ 3700 만원", "4100 ~ 5000 만원"]
language_list = ["python","javascript","java","c++"]
content_list = ["서버 백엔드 엔지니어", "AI 개발자", "웹 프론트엔드 개발자", "UI/UX 디자이너"]
location_list = ["경기도 성남시 분당구", "서울특별시 강남구", "서울특별시 서초구", "서울특별시 동작구", "제주특별자치도 서귀포구", "대전광역시 유성구"]
career_list = ["신입", "경력"]

class Command(BaseCommand):
    help = 'Populates the database. Deletes old entries'

    def handle(self, *args, **options):
        print("Populating...")

        
        for i in range(300):
            Post.objects.create(author=User.objects.get(is_active=True), title=random.sample(campany_list,1)[0]+str(i),content=random.sample(content_list,1)[0], language=random.sample(language_list,1)[0], salary=random.sample(salary_list,1)[0], location=random.sample(location_list,1)[0], career=random.sample(career_list,1)[0],  deadline=datetime.datetime(2021,randint(1,12),randint(1,29)))
        
        print("Done.") 