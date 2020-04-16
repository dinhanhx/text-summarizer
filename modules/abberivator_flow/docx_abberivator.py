from abberivator_flow import scriptum_abberivator as sa
import docx

def summarize(file):
	doc = docx.Document(file)
	text = []
	for para in doc.paragraphs:
	   text.append(para.text)

	seperator = ''
	return sa.summarize(str(seperator.join(text)))
