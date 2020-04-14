from abberivator_flow import scriptum_abberivator as sa
import PyPDF2

def summarize(pdf_file):
	pdfFileObj = open(pdf_file, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	num = pdfReader.numPages
	text = []
	for i in range(num):
		pageObj = pdfReader.getPage(i)
		text.append(pageObj.extractText())

	# print(text)
	seperator = ', '
	return sa.summarize(seperator.join(text))
