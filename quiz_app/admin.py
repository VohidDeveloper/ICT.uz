from django.contrib import admin

from .models import Quiz

class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_answer')
admin.site.register(Quiz, QuizAdmin)