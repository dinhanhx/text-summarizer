from flask import Flask, render_template, request, send_file
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/text-summarizer')
def ignite():
   return render_template('main-page.html')


@app.route('/text-summarizer',methods = ['POST', 'GET'])
def result_text():
	if request.method == 'POST':
		result = request.form
		text_tring = result['Text']
		from abberivator_flow import scriptum_abberivator as sa
		out_text_file = open('out.txt', 'w')
		out_text_file.write(sa.summarize(text_tring))
		out_text_file.close()
		return send_file('out.txt', as_attachment=True)


@app.route('/text-summarizer',methods = ['POST', 'GET'])
def result_wiki():
	if request.method == 'POST':
		result = request.form
		url = result['Text']
		if "en.wikipedia.org/wiki/" in url:
			import requests
			req = requests.get(url)
			if req.status_code == 200:
				from abberivator_flow import wikipedia_abberivator as wa
				out_text_file = open('out.txt', 'w')
				out_text_file.write(wa.summarize(url))
				out_text_file.close()
				return send_file('out.txt', as_attachment=True)
			else:
				return render_template('main-page.html')
		else:
			return render_template('main-page.html')


@app.route('/text-summarizer',methods = ['POST', 'GET'])
def result_pdff():
	if request.method == 'POST':
		f = request.files['file']
		f.save(secure_filename(f.filename))
		from abberivator_flow import document_abberivator as da
		out_text_file = open('out.txt', 'w')
		out_text_file.write(da.summarize(f.filename))
		out_text_file.close()
		return send_file('out.txt', as_attachment=True)


if __name__ == '__main__':
	app.config["TEMPLATES_AUTO_RELOAD"] = True
	app.run(debug = False, host= '0.0.0.0')
