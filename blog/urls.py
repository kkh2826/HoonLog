from django.urls import path
from . import views

urlpatterns = [
    # FBV 형태
    #path('', views.index),
    #path('<int:pk>/', views.single_post_page),

    # CBV 형태
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('category/<str:slug>/', views.category_page),
    path('tag/<str:slug>/', views.tag_page),
    path('create_post/', views.PostCreate.as_view()),
]
