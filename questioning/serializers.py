from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.utils import timezone

from .models import (
    Responder,
    Survey,
    ResponderAnswer,
    Question,
    QuestionAnswer
)


class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    answer = QuestionAnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ['survey', 'type', 'text', 'answer']


class CreateSurveySerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=True)

    class Meta:
        model = Survey
        exclude = ['create_at', 'is_active', 'responders']
    
    def validate(self, attrs):
        if attrs['start_date'] > attrs['end_date']:
            raise ValidationError("Start date cannot be after end date")
        return attrs


class CreateResponderAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponderAnswer
        fields = '__all__'

    def create(self, validated_data):
        Responder.objects.get_or_create(id=validated_data.get('responder'))
        return super().create(validated_data)


class UpdateSurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        exclude = ['create_at', 'is_active', 'responders', 'start_date']
    
    def validate(self, attrs):
        if timezone.now() > attrs['end_date']:
            raise ValidationError("you cannot change a completed survey")
        return attrs


class ResponderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responder
        fields = '__all__'


class ResponderAnswerSerializer(serializers.Serializer):
    resp_answer = CreateResponderAnswerSerializer(many=True)
