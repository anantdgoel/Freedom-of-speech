from gtts import gTTS

def generateAudio(text, file_name='test', lang='en'):
    """ Generate audio

    Args:
        text: Text to be spoken (written to file instead)
        lang: ISO 639-1 language code (supported by the Google Text to Speech
        API) to speak in. Check https://github.com/pndurette/gTTS for list of
        supported langs
    """
    tts = gTTS(text=text, lang=lang)
    tts.save("./generated-audio/{:s}.mp3".format(file_name))
    print('Finished generating audio for text: {:s}'.format(text))

generateAudio("Hello World")
