from django.contrib import admin

from .models import *

class HomeWelcomeAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'button_title', 'button_link']
admin.site.register(HomeWelcome, HomeWelcomeAdmin)

class HomeYonalishlarAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'button_title', 'button_link']
admin.site.register(HomeYonalishlar, HomeYonalishlarAdmin)

class HomeYonalishlarDivsAdmin(admin.ModelAdmin):
    list_display = ['title', 'svg', 'body']
admin.site.register(HomeYonalishlarDivs, HomeYonalishlarDivsAdmin)

class HomeMavjudYonalishlarAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', 'cap_title', 'body', 'letter']
admin.site.register(HomeMavjudYonalishlar, HomeMavjudYonalishlarAdmin)

class HomeAboutMeAdmin(admin.ModelAdmin):
    list_display = ['title', 'cap_title', 'image1', 'image2', 'body']
admin.site.register(HomeAboutMe, HomeAboutMeAdmin)

class HomeMehnatFaoliyatimAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'button_title', 'button_link']
admin.site.register(HomeMehnatFaoliyatim, HomeMehnatFaoliyatimAdmin)

class HomeMehnatFaoliyatiDivsAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'year']
admin.site.register(HomeMehnatFaoliyatiDivs, HomeMehnatFaoliyatiDivsAdmin)

class HomeAppAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'image1', 'image2']
admin.site.register(HomeApp, HomeAppAdmin)

class HomeTelegramGroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'button_title', 'button_link']
admin.site.register(HomeTelegramGroup, HomeTelegramGroupAdmin)

class HomeQuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'button_title', 'button_link']
admin.site.register(HomeQuestion, HomeQuestionAdmin)

class FileAdmin(admin.ModelAdmin):
    list_display = ['title', 'file']
admin.site.register(File, FileAdmin)