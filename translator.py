from texttotext import translate
from speechtotext import getText
from texttospeech import generateAudio
import subprocess

def getAudio(input_file_name, lang):
    text = getText(input_file_name)
    translated = translate(text, out_lang=lang)
    print(translated)
    generateAudio(translated, lang=lang)
    print("Finished getting audio in ", lang)

def attachVideo():
    command = "ffmpeg -i ./resources/test.mp4 -vcodec copy -an output.mp4"
    subprocess.call(command, shell=True)
    command = "ffmpeg -i output.mp4 -itsoffset 00:00:03.2 -i ./generated-audio/test.wav -c copy output.mkv"
    subprocess.call(command, shell=True)

getAudio("audio.wav", "fr")
attachVideo()
