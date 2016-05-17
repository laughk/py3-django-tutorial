from django.contrib import admin

from .models import Choice, Question

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, { 'fields': ['question_text']}),
        ('Date infomation' , { 'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
