from abberivator_flow import pdf_abberivator as pdf_a
from abberivator_flow import docx_abberivator as docx_a
from abberivator_flow import odt_abberivator as odt_a

import os

def check_extension(file_path):
    extension = os.path.splitext(path)[-1]
    return extension.replace(".", "")

def summarize(file_path):
    extension = check_extension(file_path)
    if extension == 'odt':
        return odt_a.summarize(file_path)

    if extension == 'docx':
        return docx_a.summarize(file_path)

    if extension == 'pdf':
        return pdf_a.summarize(file_path)
