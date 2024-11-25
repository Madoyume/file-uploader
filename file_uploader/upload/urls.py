from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_image, name='upload'),
    path('<int:pk>/', views.display_image, name='display_image'),
]