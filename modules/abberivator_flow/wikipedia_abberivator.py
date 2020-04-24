import bs4 as bs
import urllib.request
import re
import nltk
import heapq

def check_url(url):
	if "en.wikipedia.org/wiki/" in url:
		import requests
		req = requests.get(url)
		if req.status_code == 200:
			return True
		else:
			return False
	else:
		return False


def summarize(url):
	if check_url(url) == True:
		scraped_data = urllib.request.urlopen(url)
		article = scraped_data.read()
		parsed_article = bs.BeautifulSoup(article,'lxml')
		paragraphs = parsed_article.find_all('p')
		article_text = ""
		for p in paragraphs:
			article_text += p.text

		article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
		article_text = re.sub(r'\s+', ' ', article_text)
		formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text)
		formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

		sentence_list = nltk.sent_tokenize(article_text)

		stopwords = nltk.corpus.stopwords.words('english')

		word_frequencies = {}
		for word in nltk.word_tokenize(formatted_article_text):
			if word not in stopwords:
				if word not in word_frequencies.keys():
					word_frequencies[word] = 1
				else:
					word_frequencies[word] += 1

		maximum_frequncy = max(word_frequencies.values())

		for word in word_frequencies.keys():
			word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

		sentence_scores = {}
		for sent in sentence_list:
			for word in nltk.word_tokenize(sent.lower()):
				if word in word_frequencies.keys():
					if len(sent.split(' ')) < 30:
						if sent not in sentence_scores.keys():
							sentence_scores[sent] = word_frequencies[word]
						else:
							sentence_scores[sent] += word_frequencies[word]

		summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

		return ' '.join(summary_sentences)
	else:
		return ''
