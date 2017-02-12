import os
import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1
import subprocess

video_file = os.path.join(
    os.path.dirname(__file__),
    'resources',
    'test.mp4')

command = "ffmpeg -i "+video_file+" -ab 160k -ac 2 -ar 44100 -vn ./resources/audio.wav"

subprocess.call(command, shell=True)


speech_to_text = SpeechToTextV1(
    username='22ccdf7d-47bb-40fe-b175-4d2cff460f85',
    password='PLPP00eicu2P',
    x_watson_learning_opt_out=False
)

# print(json.dumps(speech_to_text.models(), indent=2))
#
# print(json.dumps(speech_to_text.get_model('en-US_BroadbandModel'), indent=2))

with open(join(dirname(__file__), './resources/audio.wav'),
          'rb') as audio_file:
    print(json.dumps(speech_to_text.recognize(
        audio_file, content_type='audio/wav', timestamps=True,
        word_confidence=True),
        indent=2))
