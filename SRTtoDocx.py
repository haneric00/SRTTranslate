# from pip._vendor import requests
# requests.__version__
# from collections import OrderedDict
from functools import lru_cache
import os
import pysrt
from deepl import Translator

@lru_cache(maxsize=1000)
def srt_translate(srt_file, target_lang):
    '''
    Translates the captions in an existing .srt file to the target language

    Args:
    srt_file: the path to the .srt file
    target_lang: the language code for the target language (e.g. 'JA' for Japanese)
    '''
    subs = pysrt.open(srt_file)
    translator = Translator(os.environ['08e6b577-f6fc-ba7b-04ca-05d4729c1232:fx'])
    for sub in subs:
        sub.text = translator.translate_text(sub.text, target_lang = target_lang)
    new_srt_file = srt_file[:-4] + '-' + target_lang + '.srt'
    subs.save(new_srt_file)
    print('done')

def main():
    # Example usage
    srt_translate('file.srt', 'KO')

if __name__ == '__main__':
    main()
# class TranslationCache:
#     def __init__(self, max_size=1000):
#         self.cache = OrderedDict()
#         self.max_size = max_size
    

#     def get_translation(self, text):
#         if text in self.cache:
#             # Move the accessed item to the end to mark it as most recently used
#             self.cache.move_to_end(text)
#             return self.cache[text]
#         else:
#             return None
#     @lru_cache(maxsize = 1000)
#     def add_translation(self, text, translation):
#         if len(self.cache) >= self.max_size:
#             # Remove the least recently used item from the cache
#             self.cache.popitem(last=False)
#         self.cache[text] = translation
