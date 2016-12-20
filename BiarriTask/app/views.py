"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Play,Speaker,Line
from BiarriTask.serializers import PlaySerializer,SpeakerSerializer,LineSerializer


class SpeakerView(APIView):

    def get_items(self, **kwargs):
        if 'key' in kwargs and 'value' in kwargs:
            items = self.get_objects(kwargs['key'], kwargs['value'])
        else:
            items = Speaker.objects.all()
        return items

    def get_objects(self, key, value):
        try:
            if key.lower() == 'name':
                items = Speaker.objects.filter(name=str(value))
            else:
                items = Speaker.objects.filter(id=int(value))
            return items
        except Speaker.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, **kwargs):
        items = self.get_items(**kwargs)
        serializer = SpeakerSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, **kwargs):
        items = self.get_items(**kwargs)
        serializer = SpeakerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, **kwargs):
        items = self.get_items(**kwargs)
        serializer = SpeakerSerializer(items, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, **kwargs):
        items = self.get_items(**kwargs)
        items.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PlayView(APIView):

    def get_items(self, **kwargs):
        if 'key' in kwargs and 'value' in kwargs:
            items = self.get_objects(kwargs['key'], kwargs['value'])
        else:
            items = Play.objects.all()
        return items

    def get_objects(self, key, value):
        try:
            if key.lower() == 'name':
                items = Play.objects.filter(name=str(value))
            
            elif key.lower() == 'author':
                items = Play.objects.filter(author=str(value))
            else:
                items = Play.objects.filter(id=int(value))
            return items
        except Play.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, **kwargs):
        items = self.get_items(**kwargs)
        serializer = PlaySerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, **kwargs):
        items = self.get_items(**kwargs)
        serializer = PlaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, **kwargs):
        items = self.get_items(**kwargs)
        serializer = PlaySerializer(items, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, **kwargs):
        items = self.get_items(**kwargs)
        items.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LineView(APIView):

    def get_items(self, **kwargs):
        if 'key' in kwargs and 'value' in kwargs:
            items = self.get_objects(kwargs['key'], kwargs['value'])
        else:
            items = Line.objects.order_by('id').all()
            if 'limit' in kwargs:
                items = items[:int(kwargs['limit'])]
        return items

    def get_objects(self, key, value):
        try:
            if key.lower() == 'number':
                items = Line.objects.filter(number=str(value))
            
            elif key.lower() == 'text':
                items = Line.objects.filter(text__icontains=str(value))
                #items.append(Line.objects.filter(text__istartswith=str(value)))
                #items.append(Line.objects.filter(text__endswith=str(value)))
            elif key.lower() == 'speaker':
                items = Line.objects.filter(speaker=Speaker.objects.filter(name=str(value)))
            elif key.lower() == 'play':
                items = Line.objects.filter(play=Play.objects.filter(name=str(value)))
            elif key.lower() == 'speech':
                items = Line.objects.filter(speech_no=int(value))
            else:
                items = Line.objects.filter(id=int(value))
            return items
        except Line.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, **kwargs):
        items = self.get_items(**kwargs)
        serializer = LineSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, **kwargs):
        items = self.get_items(**kwargs)
        serializer = LineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, **kwargs):
        items = self.get_items(**kwargs)
        serializer = LineSerializer(items, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, **kwargs):
        items = self.get_items(**kwargs)
        items.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def apitest(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/apitest.html'
        )