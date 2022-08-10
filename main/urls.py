from django.urls import path
from .views import home_view,post_detail_view,post_delete_view,post_create_view


urlpatterns = [
    path('', home_view, name='index'),
    path('post/detail/<int:id>/', post_detail_view, name='detail'),
    path('delete/<int:id>/', post_delete_view, name='post_delete'),
    path('create/post/', post_create_view, name='post_create')
]