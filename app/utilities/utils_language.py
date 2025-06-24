import pandas as pd
from textblob import TextBlob
#from textblob.translate import Translator
from time import sleep
from googletrans import Translator

def get_language(tweet):
    return TextBlob(tweet).detect_language()

def translate_to_eng(paragraph):
    paragraph = str(paragraph).strip().split('.')
    translated = []
    print(paragraph)
    translator = Translator()

    for sentence in paragraph:
        try:
            sleep(1.0)
            sentence = sentence.strip()
            #print(translator.detect(sentence).lang)
            sentence_translated = translator.translate(sentence)
            translated.append(sentence_translated.text)
            sleep(1.0)
        except Exception as e:
            print(e)
    # try:
    #     translator = Translator()
    #     #translator = Translator(service_urls=['translate.googleapis.com'])
    #     print("translated: before")
    #     translated = translator.translate(paragraph)
    #     print("translated: ", translated.text)
    # except Exception as e:
    #     print(e)

    return translated

def remove_enter(row):
    row = row.replace('\n', ' ')
    return row







