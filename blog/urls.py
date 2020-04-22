from django.urls import path
from . import views

urlpatterns = [
    path('', views.allblogs, name='bloghome'),
    path('<int:blog_id>/', views.detail, name='detail'),
]
