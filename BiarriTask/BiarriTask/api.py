from tastypie.resources import ModelResource
from app.models import Play, Speaker, Line

class PlayResource(ModelResource):
    class Meta:
        queryset = Play.objects.all()
        resource_name = 'play'

class SpeakerResource(ModelResource):
    class Meta:
        queryset = Speaker.objects.all()
        resource_name = 'speaker'

class LineResource(ModelResource):
    class Meta:
        queryset = Line.objects.all()
        resource_name = 'line'