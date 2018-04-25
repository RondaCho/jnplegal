from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post

notice_list = ListView.as_view(model=Post, paginate_by=20)

notice_detail = DetailView.as_view(model=Post)