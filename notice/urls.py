from notice import views
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('post/', views.post, name='post'),
    path('detail/', views.detail, name='detail'),
    path('show/', views.show, name='show'),
    path('<int:notice_id>/', views.detail, name='detail'),
    path('<int:pk>/edit/',views.edit, name='edit'),
    path('<int:pk>/delete/',views.delete, name='delete'),
    path('download/<int:pk>',views.download,name='download'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)