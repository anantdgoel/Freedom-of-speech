import os
import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1

speech_to_text = SpeechToTextV1(
    username='22ccdf7d-47bb-40fe-b175-4d2cff460f85',
    password='PLPP00eicu2P',
    x_watson_learning_opt_out=False
)

def generateTranscript(input_file_name, output_file_name='test.txt'):
    text_file = open("./resources/" + output_file_name, "w")
    text_file.write(getText(input_file_name))
    text_file.close()
    print('Finished generating transcript for audio: {:s}'
        .format(input_file_name))

def getText(file_name):
    with open(join(dirname(__file__), './resources/' + file_name),
              'rb') as audio_file:
        data = speech_to_text.recognize(
            audio_file, content_type='audio/wav', timestamps=True,
            word_confidence=True)
        return json.dumps(data['results'][0]['alternatives'][0]['transcript'],
            indent=2)
