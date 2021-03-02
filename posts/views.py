
from django.views import View
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from accounts.models import User
from django.core import serializers
from django.forms.models import model_to_dict
import json
# Create your views here.

class ScrollView(View):
    pass


class BoardScrollView(View):
    
    def get(self, request):
        page = request.GET.get('page', 1)
        posts_list = Post.objects.order_by('-pub_date')
        paginator = Paginator(posts_list, 10)  # 페이지당 10개씩 보여주기
        board = paginator.get_page(page)

        print(type(board))
        context = {'board': board}
        return render(request, 'posts/board-job.html',  {'board': board})

def scroll_posts(request):

    print("scroll_posts")

    try:
        counter = int(request.POST.get('counter',None))
        posts_list = Post.objects.order_by('-pub_date')
        paginator = Paginator(posts_list, 10)  # 페이지당 10개씩 보여주기
        board = paginator.get_page(counter)
        print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
        print(board)
        print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
        board = serializers.serialize('json', board)
        return JsonResponse({'msg': "success","board":board}, status=200)
    except Exception as Error:
        print(Error)
        return JsonResponse({'msg': "error"}, status=200)



