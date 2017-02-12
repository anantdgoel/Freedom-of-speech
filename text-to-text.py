import json
from watson_developer_cloud import LanguageTranslatorV2 as LanguageTranslator

language_translator = LanguageTranslator(
    username='be2f6ef1-f3e1-4976-a2e6-8c59d0736d65',
    password='chbN8WUGDph4')

def translate(text, in_lang='en', out_lang='es'):
    translation = language_translator.translate(
        text=text,
        source=in_lang,
        target=out_lang)
    return json.dumps(translation, indent=2, ensure_ascii=False)

print(translate('bitch'))
