from abberivator_flow import pdf_abberivator as pdf_a
from abberivator_flow import docx_abberivator as docx_a
from abberivator_flow import odt_abberivator as odt_a

import os

def get_extension(file_path):
    extension = os.path.splitext(file_path)[-1]
    return extension.replace(".", "")

def summarize(file_path):
    extension = get_extension(file_path)
    extension_list = ['odt', 'docx', 'pdf']
    if extension not in extension_list:
    	return "File not supported"

    if extension == 'odt':
        return odt_a.summarize(file_path)

    if extension == 'docx':
        return docx_a.summarize(file_path)

    if extension == 'pdf':
        return pdf_a.summarize(file_path)
