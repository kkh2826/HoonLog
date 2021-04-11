from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.

#######################################
####### FBV 형태로 구현한 코드 ###########
#######################################
# def index(request):
#     posts = Post.objects.all().order_by('-pk')
#
#     return render(
#         request,
#         'blog/post_list.html',
#         {
#             'posts': posts,
#         }
#     )
#
#
# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#
#     return render(
#         request,
#         'blog/post_detail.html',
#         {
#             'post': post,
#         }
#     )
#######################################

#######################################
####### CBV 형태로 구현한 코드 ###########
#######################################
class PostList(ListView):
    model = Post
    ordering = '-pk'


class PostDetail(DetailView):
    model = Post
