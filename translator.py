from texttotext import translate
from speechtotext import getText
from texttospeech import generateAudio

def getAudio(input_file_name, lang):
    text = getText(input_file_name)
    translated = translate(text, out_lang=lang)
    print(translated)
    generateAudio(translated, lang=lang)
    print("Finished getting audio in ", lang)

getAudio("audio.wav", "fr")
