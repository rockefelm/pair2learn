# forum/urls.py

from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    # List all threads
    path('', views.ThreadListView.as_view(), name='thread_list'),
    
    # View a specific thread and its posts
    path('thread/<int:pk>/', views.ThreadDetailView.as_view(), name='thread_detail'),
    
    # Create a new thread
    path('thread/new/', views.CreateThreadView.as_view(), name='create_thread'),
    
    # Create a new post within a specific thread
    path('thread/<int:thread_id>/post/new/', views.CreatePostView.as_view(), name='create_post'),
]   