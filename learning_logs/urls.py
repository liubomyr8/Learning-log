"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Main page
    path('', views.index, name='index'),
    # Topics page
    path('topics', views.topics, name='topics'),
    # Page for a specific topic
    path('topics/<int:topic_id>', views.topic, name='topic'),
    # Add a new topic
    path('create_topic', views.new_topic, name="new_topic"),
    # Add a new entry for specific topic
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Edit entry
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
    # Add a new comment for the specific entry
    path('create_comment', views.new_comment, name="new_comment"),
    
    path('get_comments/<int:entry_id>/', views.get_comments, name='get_comments'),
    
    
]