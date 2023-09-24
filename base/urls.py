from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,UserPostListView
urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='base/login.html'), name='login'),
    path('logout/', LogoutView.as_view(
        template_name='base/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
]
