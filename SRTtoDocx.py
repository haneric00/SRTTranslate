import pysrt
from docx import Document
from docx.shared import Pt
import deepl
import os

# My API key is stored in an environment variable
translator = deepl.Translator(os.getenv("DEEPL_AUTH_KEY"))

def srt_translate(srt_file, target_lang):
    '''
    Translates the captions in an existing .srt file to the target language

    Args:
    srt_file: the path to the .srt file
    target_lang: the language code for the target language (e.g. 'JA' for Japanese)
    '''
    subs = pysrt.open(srt_file)
    for sub in subs:
        sub.text = translator.translate_text(sub.text, target_lang=target_lang)
    new_srt_file = srt_file[:-4] + '-' + target_lang + '.srt'
    subs.save(new_srt_file)
    print('done')

def add_to_glossary(glossary_name, word_dict):
    pass

def translate_with_glossary(docx_file, glossary_name):
    pass

    

def main():
    srt_translate('./day_in_my_life_7.17.srt', 'KO')

if __name__ == '__main__':
    main()