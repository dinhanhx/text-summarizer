import nltk
nltk.download('stopwords')
nltk.download('punkt')
from abberivator_flow import scriptum_abberivator as sa
from abberivator_flow import wikipedia_abberivator as wa
from abberivator_flow import pdf_abberivator as pa

## Test raw file text
# text_file = open('A_long_text.txt', 'r')
# text = text_file.read()
# text_file.close()

# out_text_file = open('A_long_text_sum.txt', 'w')
# out_text_file.write(sa.summarize(text))
# out_text_file.close()


## Test a wikipedia url
# url = 'https://en.wikipedia.org/wiki/Science_of_Logic'
# out_text_file = open('A_wiki_sum.txt', 'w')
# out_text_file.write(wa.summarize(url))
# out_text_file.close()

## Test a pdf file
# pdf_file = 'sample.pdf'
# out_text_file = open('A_pdf_sum.txt', 'w')
# out_text_file.write(pa.summarize(pdf_file))
# out_text_file.close()

## Test a doc file
from abberivator_flow import scriptum_abberivator as sa
import textract

def summarize(doc_file):
	text = textract.process(doc_file)
	seperator = ', '
	return sa.summarize(seperator.join(text))
