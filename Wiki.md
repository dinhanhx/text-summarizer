# Welcome to the text-summarizer wiki!
## Table of contents
- [Introduction](#1-introduction)
- [Installation](#2-installation)
- [Usage](#3-usage)
- [Library abberivator_flow of backend](#4-library-abberivator_flow)
- [Tree structure of frontend](#5-tree-structure-of-frontend)

## 1. Introduction
The text-summarizer Software is a tool to analyze text documents and simplify them to only the key words. It captures most significant concepts, providing a concise overview, which can be useful in studying and memorizing for the user. The software is applicable to a myriad of documents such as articles or textbooks; and supports typical text files or online articles.

## 2. Installation
### Warning
If you git clone or download the repos, you will have nightly-build product.

If you download 'Release' section, you will have stable product.
### Protocol
```
pip install -r requirements.txt .
```
Run this command line in 'modules' folder to set up all packages.

```
python nltk_downloads.py
```
Run this command line in 'modules' folder to set up all components related to [nltk](https://www.nltk.org/).

## 3. Usage
### Ignite the app
```
python text-sum-core.py
```
Run this command line in 'webapp' folder to start the application.

Open your favorite browser and go to this [link.](http://localhost:5000/text-summarizer)
```
http://localhost:5000/text-summarizer
```
### Use the app
It's quite easy to use.

The web app will return you as text file named 'out.txt'

 ___Plain text (in English)___

You can paste your long text in the first input box then click summarize this.

___Wikipedia article (in English)___

You can paste a link to an English Wikipedia article such as [this](https://en.wikipedia.org/wiki/Loss_function) or [that](https://en.wikipedia.org/wiki/Communist_Party_of_Georgia_(Soviet_Union)) in the second input box then click summarize this.
```
https://en.wikipedia.org/wiki/Communist_Party_of_Georgia_(Soviet_Union)
https://en.wikipedia.org/wiki/Loss_function
```
___Documents (Purely created and in English)___

You can upload a .pdf, .odt, .docx file then click summarize this.

## 4. Library abberivator_flow
This library has 3 main modules
```python
from abberivator_flow import scriptum_abberivator as sa
from abberivator_flow import wikipedia_abberivator as wa
from abberivator_flow import document_abberivator as da
```
```python
long_str = "Imagine you have a paragraph here not this short string"
output_str = sa.summarize(long_str)
```
```python
url = "https://en.wikipedia.org/wiki/Loss_function"
output_str = wa.summarize(url)
```
```python
file_path = "your_file.odt" # your_file.docx or your_file.pdf
output_str = da.summarize(file_path)
```
## 5. Tree structure of frontend
Tree structure of folder 'webapp'
```
|   text-sum-core.py
|   
+---static
|   |   a.jpg
|   |   b.jpg
|   |   
|   +---css
|   |       style.css
|   |       
|   \---js
|           main.js
|           
\---templates
        main-page.html
```
