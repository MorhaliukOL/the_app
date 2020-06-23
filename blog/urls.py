from django.urls import path
from .views import blog_view, write_post, view_post


urlpatterns = [
    path('', blog_view, name='blog'),
    path('write', write_post, name='write-post'),
    path('read/<int:pk>', view_post, name='view-post'),
]