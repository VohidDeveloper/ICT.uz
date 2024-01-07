from django.urls import path

from .views import video_page, slayd_page, maruza_page, amaliy_page, test_page, \
    download_maruza, download_amaliy, download_taqdimot

urlpatterns = [
    path('video/', video_page, name='video_page'),
    path('slayd/', slayd_page, name='slayd_page'),
    path('maruza/', maruza_page, name='maruza_page'),
    path('amaliy/', amaliy_page, name='amaliy_page'),
    path('test/', test_page, name='test_page'),

    # Download count
    path('download-maruza/<int:pk>/', download_maruza, name='download_maruza'),
    path('download-amaliy/<int:pk>/', download_amaliy, name='download_amaliy'),
    path('download-taqdimot/<int:pk>/', download_taqdimot, name='download_taqdimot'),
]