from abberivator_flow import scriptum_abberivator as sa
from odf import text, teletype
from odf.opendocument import load

def summarize(odt_file):
    text_doc = load(odt_file)
    allparas = text_doc.getElementsByType(text.P)
    raw_text = []
    for para in allparas:
        raw_text.append(teletype.extractText(para))

    seperator = ''
	return sa.summarize(str(seperator.join(raw_text)))
