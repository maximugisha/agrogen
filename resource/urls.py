# urls.py

from django.urls import path
from .views import create_resource, index, list_resources, create_post, resource_detail, post_detail, list_posts, \
    create_post_comment, like_post, dislike_post
from .views import CreatePostView, CreateAttachmentView


urlpatterns = [
    path('index', index, name='index'),  # Define URL pattern for the homepage
    path('resources/', list_resources, name='list_resources'),
    path('create_resource/', create_resource, name='create_resource'),
    path('<int:resource_id>/', resource_detail, name='view_resource'),
    path('posts/', list_posts, name='list_posts'),
    path('api/create_post/', CreatePostView.as_view(), name='api_create_post'),
    path('api/create_attachment/', CreateAttachmentView.as_view(), name='api_create_attachment'),
    path('create_post/', create_post, name='create_post'),
    path('post/<int:post_id>/comment/', create_post_comment, name='comment'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('post/<int:post_id>/like/', like_post, name='like_post'),
    path('post/<int:post_id>/dislike/', dislike_post, name='dislike_post'),

    # Add other URL patterns as needed
]
