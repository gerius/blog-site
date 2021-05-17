from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path
from django.views.generic import RedirectView

from . import views
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, CommentCreateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),

    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.png'))),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register', views.register, name='register'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('comment', CommentCreateView.as_view(), name='comment'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home')
]
