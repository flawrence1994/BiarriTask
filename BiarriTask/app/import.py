##test
import os, sys

proj_path = os.getcwd()
# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BiarriTask.settings")
sys.path.append(proj_path)

# This is so my local_settings.py gets loaded.
os.chdir(proj_path)

# This is so models get loaded.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()



####


import json, os, django
#from django.conf import settings
#settings.configure()
django.setup()

#print(settings.DATABASES)

from app.models import Speaker,Play,Line

data=[]
with open(os.path.join(os.getcwd(),'app','static','resources','henry_iv.json'),'r') as f:
    for line in f:
        data.append(json.loads(line))
play=data[0]

db_play = Play.objects.filter(name=play[0]['play_name'],author='William Shakespeare').first()
if db_play is None:
    db_play = Play(name=play[0]['play_name'],author='William Shakespeare')
    db_play.save()
for line in play:
    db_speaker = Speaker.objects.filter(name=line['speaker']).first()
    if db_speaker is None:
        db_speaker = Speaker(name=line['speaker'])
        db_speaker.save()
    speech_number = None
    if line['speech_number'] != '':
        speech_number = line['speech_number']
    db_line = Line(id=line['line_id'],number=line['line_number'],text=line['text_entry'],speech_no=speech_number,speaker=db_speaker,play=db_play)
    db_line.save()