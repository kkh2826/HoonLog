from django.urls import path
from . import views

urlpatterns = [

    # CBV 형태

    # 게시물 리스트
    path('', views.PostList.as_view()),
    # 특정 게시물
    path('<int:pk>/', views.PostDetail.as_view()),
    # 특정 카테고리 게시물
    path('category/<str:slug>/', views.category_page),
    # 특정 태크 게시물
    path('tag/<str:slug>/', views.tag_page),
    # 게시물 생성 
    path('create_post/', views.PostCreate.as_view()),
    # 게시물 수정
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    # 특정 게시물에 대해 댓글 생성
    path('<int:pk>/new_comment/', views.new_comment),
    # 댓글 수정
    path('update_comment/<int:pk>/', views.CommentUpdate.as_view()),
    # 댓글 삭제
    path('delete_comment/<int:pk>/', views.delete_comment),
    # 특정 키워드로 게시물 찾기
    path('search/<str:q>/', views.PostSearch.as_view()),
]
