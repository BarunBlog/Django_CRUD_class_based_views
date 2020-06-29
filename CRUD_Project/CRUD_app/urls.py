from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_blog/', views.CreateBlog.as_view(), name='create_blog'),
    path('blog_list/', views.BlogList.as_view(), name='blog_list'),
    path('blog_detail/<pk>', views.BlogDetail.as_view(), name='blog_detail'),
    path('update_blog/<pk>', views.UpdateBlog.as_view(), name='update_blog'),
    path('delete_blog/<pk>', views.DeleteBlog.as_view(), name='delete_blog'),
]
