from notice import views
from django.contrib import admin
from django.urls import path

urlpatterns=[
    path('post/', views.post, name='post'),
    path('detail/', views.detail, name='detail'),
   # path('show/', views.show, name='show'),
    path('<int:notice_id>/', views.detail, name='detail'),
    path('<int:pk>/edit/',views.edit, name='edit'),
    path('<int:pk>/delete/',views.delete, name='delete'),
    path('post_list/',views.post_list, name='post_list'),
]