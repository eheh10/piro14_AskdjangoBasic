from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import Post

post_list = ListView.as_view(model=Post)

post_detail = DetailView.as_view(model=Post)

@login_required
def post_new(request):
    pass