from django.urls import path
from . import views
# from .views import EventListView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('memories/', views.memories, name='memories'),
    path('register/', views.register, name='register'),
    path('memory/<int:memory_pk>/', views.detail, name='detail'),
    path('delete/<int:memory_pk>/', views.delete, name='delete'),
    path('new/', views.NewMem, name='new'),
    path('update/<int:memory_pk>/', views.UpdateMem, name='update'),
    path('login/', auth_views.LoginView.as_view(template_name='diaryapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='diaryapp/logout.html'), name='logout'),
]
