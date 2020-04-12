from abberivator_flow import scriptum_abberivator as sa
import docx

def summarize(file):
	doc = docx.Document(file)
	text = []
	for para in doc.paragraphs:
	   text.append(para.text)
	seperator = ', '
	return sa.summarize(seperator.join(text))

print(summarize("George_Washington_Journal_Octorber_9_1794.docx"))