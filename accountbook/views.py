from django.shortcuts import render
from django.views.generic import ListView

from accountbook.models import Category


class CategoryListView(ListView):
    model = Category    #category 테이블의 모든 category를 가져와 category_list라는 context에 담아 category_list.html에 넘김