
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
        pass