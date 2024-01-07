from django.urls import path

from .views import more_page, download_media_file

urlpatterns = [
    path('<int:category_id>/', more_page, name='more_page'),
    path('download/<int:pk>/', download_media_file, name='media_file_download'),
]