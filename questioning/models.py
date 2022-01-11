from django.db import models
from django.utils import timezone
from datetime import timedelta


class Survey(models.Model):
    owner = models.ForeignKey('Responder', on_delete=models.CASCADE, related_name='survey_owner')
    title = models.CharField('survey title', max_length=200)
    start_date = models.DateTimeField('start date time', default=timezone.now())
    end_date = models.DateTimeField('end date time', default=timezone.now()+timedelta(days=10))
    description = models.TextField('description')
    create_at = models.DateTimeField('created date time', auto_created=True, default=timezone.now())
    is_active = models.BooleanField(default=True, verbose_name='is active')
    responders = models.ManyToManyField('Responder', verbose_name='responders')

    def __str__(self) -> str:
        return self.title


class Question(models.Model):
    QUESTION_TYPE = (
        (1, 'reply by text'),
        (2, 'reply by choice'),
        (3, 'reply by multiple choices')
    )

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, verbose_name='survey')
    type = models.PositiveSmallIntegerField('type', choices=QUESTION_TYPE)
    text = models.TextField('text')

    def __str__(self) -> str:
        return self.survey
    

class QuestionAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='question')
    text = models.TextField('text')

    def __str__(self) -> str:
        return self.question


class Responder(models.Model):
    id = models.PositiveIntegerField('responder unique id', unique=True, primary_key=True)
    responded_surveys = models.ManyToManyField(Survey, verbose_name='responded surveys')

    def __str__(self) -> str:
        return str(self.id)


class ResponderAnswer(models.Model):
    responder = models.ForeignKey(Responder, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(QuestionAnswer, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.responder} -> survey'
