from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.ThreadListView.as_view(), name='thread-list'),
    path('thread/<int:pk>/', views.ThreadDetailView.as_view(), name='thread-detail'),
    path('thread/new/', views.CreateThreadView.as_view(), name='create-thread'),
    path('thread/<int:thread_id>/post/new/', views.create_post, name='create-post'),
]   