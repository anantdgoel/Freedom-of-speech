import io
import os

# Imports the Google Cloud client library
from google.cloud import speech

import subprocess

# video_file = os.path.join(
#     os.path.dirname(__file__),
#     'resources',
#     'test.mp4')
#
# command = "ffmpeg -i "+video_file+" -ab 160k -ac 2 -ar 44100 -vn ./resources/audio.wav"
#
# subprocess.call(command, shell=True)
#
# command = "ffmpeg -i ./resources/audio.wav -f s16le -acodec pcm_s16le ./resources/output.raw"
#
# subprocess.call(command, shell=True)

# Instantiates a client
speech_client = speech.Client()

# The name of the audio file to transcribe
audio_file = os.path.join(
    os.path.dirname(__file__),
    'generated-audio',
    'test.mp3')

# Loads the audio into memory
with io.open(audio_file, 'rb') as audio_file:
    content = audio_file.read()
    audio_sample = speech_client.sample(
        content,
        source_uri=None,
        encoding='LINEAR16',
        sample_rate=16000)

alternatives = [];

# Detects speech in the audio file
alternatives = speech_client.speech_api.sync_recognize(audio_sample)

for alternative in alternatives:
    print('Transcript: {}'.format(alternative.transcript))
