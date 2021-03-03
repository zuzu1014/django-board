
from django.views import View
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import JsonResponse

from .models import *
from accounts.models import User

from django.core import serializers
from django.db.models import Q


class BoardScrollView(View):

    
    def get_board_data(self, keywords=None, counter = 1):

        post_list = Post.objects.order_by("-pub_date")

        if keywords is not None:
            keywords = keywords.split(" ")
            for keyword in keywords:
                post_list = post_list.filter(Q(title__icontains=keyword) | Q(content__icontains=keyword) | Q(language__icontains=keyword) | Q(salary__icontains=keyword) | Q(location__icontains=keyword) |  Q(career__icontains=keyword))

        paginator = Paginator(post_list, 10)

        if paginator.num_pages < counter :
            return False

        board = paginator.get_page(counter)
        posts_num = len(post_list)
        board_data = {"board" : board, "posts_num" : posts_num}
        return board_data

    def get_data_num(self, keywords=None):
        post_list = Post.objects.order_by("-pub_date")
        
        data_num = {}
        
        data_num["num_python"] = post_list.filter(language="python").count()
        data_num["num_java"] = post_list.filter(language="java").count()
        data_num["num_javascript"] = post_list.filter(language="javascript").count()
        data_num["num_cpp"] = post_list.filter(language="C++").count()
        data_num["num_junior"] = post_list.filter(career="신입").count()
        data_num["num_senior"] = post_list.filter(career="경력").count()
        
        return data_num


    def get(self, request):


        keywords = request.GET.get("keywords", None)

        data_num = self.get_data_num(keywords)
        board_data = self.get_board_data(keywords)

        return render(request, 'posts/board-job.html', {"board_data" : board_data, "data_num": data_num, "keywords" : keywords})


    def post(self, request):

        keywords = request.GET.get("keywords", None)
        counter = int(request.POST.get("counter", None))

        board_data = self.get_board_data(keywords,counter)

        if board_data:
            board =  serializers.serialize('json', board_data['board'])
            return JsonResponse({'msg': "success","board":board}, status=200)
        else:
            return JsonResponse({'msg': "finish"}, status=200)





