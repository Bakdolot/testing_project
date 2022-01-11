from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import Response

from questioning.models import Responder, ResponderAnswer, Survey
from .serializers import CreateSurveySerializer, ResponderAnswerSerializer, ResponderSerializer
from .permissions import IsOwnerOrReadOnly


class CreateSurveyView(CreateAPIView):
    queryset = Survey
    serializer_class = CreateSurveySerializer

    def create(self, request, *args, **kwargs):
        Responder.objects.get_or_create(id=request.data.get('owner'))
        return super().create(request, *args, **kwargs)


class SurveyView(RetrieveUpdateDestroyAPIView):
    queryset = Survey
    serializer_class = CreateSurveySerializer
    permission_classes = [IsOwnerOrReadOnly]


class PassSurveyView(CreateAPIView):
    queryset = ResponderAnswer
    serializer_class = ResponderAnswerSerializer


class SurveyListView(ListAPIView):
    serializer_class = CreateSurveySerializer

    def get_queryset(self):
        return Survey.objects.filter(is_active=True, end_date__lt=timezone.now())


class SurveyResponderView(ListAPIView):
    serializer_class = ResponderSerializer

    def get_queryset(self):
        survey = get_object_or_404(Survey.objects.all(), pk=self.kwargs.get('survey_id'))
        return survey.responders.all()


class ResponderAnswerView(ListAPIView):
    serializer_class = ResponderAnswerSerializer

    def get_queryset(self):
        queryset = ResponderAnswer.objects.filter(
            survey__id=self.kwargs.get('survey_id'),
            responder__id=self.kwargs.get('responder_id')
            )
        return queryset


class ResponderPassServeysView(ListAPIView):
    serializer_class = CreateSurveySerializer

    def get_queryset(self):
        responder = get_object_or_404(Responder.objects.all(), pk=self.kwargs.get('responder_id'))
        return responder.responded_surveys.all()


class ResponderCreateSurveysView(ListAPIView):
    serializer_class = CreateSurveySerializer

    def get_queryset(self):
        return Survey.objects.filter(owner__id=self.kwargs.get('responder_id'))
