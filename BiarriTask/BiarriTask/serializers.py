from rest_framework import serializers
from app.models import Play,Speaker,Line

class PlaySerializer(serializers.ModelSerializer):
    class Meta:
        model=Play
        fields = "__all__" #('name', 'author')
        
class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Speaker
        fields = "__all__" #('name')
        
class LineSerializer(serializers.ModelSerializer):
    play = serializers.SlugRelatedField(read_only=True,slug_field='name')
    speaker = serializers.SlugRelatedField(read_only=True,slug_field='name')
    class Meta:
        model=Line
        fields = "__all__" #('id', 'number', 'speech_no', 'text', 'play', 'speaker')