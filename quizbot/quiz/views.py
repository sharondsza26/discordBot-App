from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Question
from .serializers import RandomQuestionSerializer


class RandomQuestion(APIView):

  def get(self, request, formate=None, **kwargs):
    # random selection of question ordered by '?' and sliced :1 Q1.
      question = Question.objects.filter().order_by('?')[:1]
    #   preparing data to send to bot
      serializer = RandomQuestionSerializer(question, many=True)
      return Response(serializer.data) 