
from django.views import View
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import JsonResponse

from .models import *
from accounts.models import User


# Create your views here.

class ScrollView(View):
    pass


class BoardView(View):
    
    def get(self, request):
        page = request.GET.get('page', 1)
        posts_list = Post.objects.order_by('-pub_date')
        
        paginator = Paginator(posts_list, 10)  # 페이지당 10개씩 보여주기
        page_obj = paginator.get_page(page)
        print(page_obj.count)

        context = {'posts_list': page_obj}
        return render(request, 'posts/board.html', context)