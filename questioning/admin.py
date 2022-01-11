from django.contrib import admin
from nested_admin import nested

from .models import (
    Survey,
    Question,
    QuestionAnswer,
    Responder,
    ResponderAnswer
)

 
class QuestionAnswerInline(nested.NestedTabularInline):
    model = QuestionAnswer
    extra = 0


class QuestionInline(nested.NestedTabularInline):
    model = Question
    inlines = [QuestionAnswerInline]
    extra = 0


@admin.register(Survey)
class SurveyAdmin(nested.NestedModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'description', 'is_active')
    list_display_links = list_display
    inlines = [QuestionInline]
    readonly_fields = ('create_at',)


@admin.register(ResponderAnswer)
class ResponderAnswerAdmin(admin.ModelAdmin):
    list_display = ['responder', 'survey']
    list_display_links = list_display
    list_filter = ['responder', 'survey', 'question', 'answer']


admin.site.register(Responder)
