from abberivator_flow import scriptum_abberivator as sa
import docx

def summarize(doc_file):
	doc = docx.Document(doc_file)
	text = []
	for para in docparagraphs:
	   text.append(para.text)

	seperator = ', '
	return sa.summarize(seperator.join(text))
