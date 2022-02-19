from rest_framework import serializers
from .models import Question, Answer

class AnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Answer
        fields = [
            'id',
            'answer',
            'is_correct',
        ]


class RandomQuestionSerializer(serializers.ModelSerializer):
    # calling answer serializer to get answer
    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:
        # packing up the question and answer and sending it at the same time
        model = Question
        # filtering fields
        fields = [
            'title','answer',
        ]