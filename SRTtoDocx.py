import pysrt
from docx import Document
import deepl
import os

# My API key is stored in an environment variable
translator = deepl.Translator(os.getenv("DEEPL_AUTH_KEY"))

def srt_to_docx(srt_file):
    subs = pysrt.open(srt_file)
    doc = Document()
    for sub in subs:
        doc.add_paragraph(sub.text)
    doc.save('file.docx')

def translate_docx(docx_file, target_lang):
    pass

def add_to_glossary(glossary_name, word_dict):
    pass

def translate_with_glossary(docx_file, glossary_name):
    pass