from django.contrib import admin

from .models import *

class OneHeaderAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', 'is_submenu']
admin.site.register(OneHeader, OneHeaderAdmin)

class TwoHeaderAdmin(admin.ModelAdmin):
    list_display = ['title', 'one_header', 'link', 'is_submenu']
admin.site.register(TwoHeader, TwoHeaderAdmin)

class LogoSettingsAdmin(admin.ModelAdmin):
    list_display = ['title', 'logo']
admin.site.register(LogoSettings, LogoSettingsAdmin)

class RightButtonSettingsAdmin(admin.ModelAdmin):
    list_display = ['title', 'link']
admin.site.register(RightButtonSettings, RightButtonSettingsAdmin)

class FooterSettingsAdmin(admin.ModelAdmin):
    list_display = ['title']
admin.site.register(FooterSettings, FooterSettingsAdmin)

class SocialSettingsAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'link']
admin.site.register(SocialSettings, SocialSettingsAdmin)

class PhoneEmailSettingsAdmin(admin.ModelAdmin):
    list_display = ['phone1', 'phone2', 'email1', 'email2']
admin.site.register(PhoneEmailSettings, PhoneEmailSettingsAdmin)

class SeoSettingsAdmin(admin.ModelAdmin):
    list_display = ['title', 'keywords', 'description', 'author', 'favicon']
admin.site.register(SeoSettings, SeoSettingsAdmin)

class TelegramBotSettingsAdmin(admin.ModelAdmin):
    list_display = ['title', 'token', 'user_id']
admin.site.register(TelegramBotSettings, TelegramBotSettingsAdmin)