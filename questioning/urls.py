from django.urls import path

from .views import (
    CreateSurveyView,
    SurveyView, 
    SurveyListView,
    SurveyResponderView,
    ResponderAnswerView,
    ResponderPassServeysView,
    ResponderCreateSurveysView,
    PassSurveyView
)

urlpatterns = [
    path('create/', CreateSurveyView.as_view()),
    path('survey/<int:pk>/', SurveyView.as_view()),
    path('survey/list/', SurveyListView.as_view()),
    path('survey/passed/<int:survey_id>/', SurveyResponderView.as_view()),
    path('responder/<int:survey_id>/<int:responder_id>/', ResponderAnswerView.as_view()),
    path('responder/passed/surveys/<int:responder_id>/', ResponderPassServeysView.as_view()),
    path('responder/create/surveys/<int:responder_id>/', ResponderCreateSurveysView.as_view()),
    path('survey/pass/', PassSurveyView.as_view())
]