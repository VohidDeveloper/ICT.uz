from django.contrib import admin

from .models import *

admin.site.register(VideoCategory)

class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'category', 'video_id', 'rating']
admin.site.register(Video, VideoAdmin)

class MaruzaAdmin(admin.ModelAdmin):
    list_display = ['title', 'fan', 'body', 'maruza_fayl']
admin.site.register(Maruza, MaruzaAdmin)

class SlaydAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'image', 'slayd_fayl']
admin.site.register(Slayd, SlaydAdmin)

class AmaliyAdmin(admin.ModelAdmin):
    list_display = ['title', 'fan', 'body', 'amaliy_fayl']
admin.site.register(Amaliy, AmaliyAdmin)

class TestlarAdmin(admin.ModelAdmin):
    list_display = ['title', 'fan', 'body', 'test_fayl']
admin.site.register(Testlar, TestlarAdmin)