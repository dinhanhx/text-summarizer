# Text summarizer
A repos for USTH SE 2020 Group 1 project. It's quite obvious in the title.

[![Img](https://img.shields.io/badge/Python-3-green)](https://www.python.org/downloads/)

[![Img](https://img.shields.io/badge/License-TheUnlicense-yellow)](https://unlicense.org/)

## Warning
If you want to contribute to this repos, please read [CONTRIBUTE.md]()

If you git clone or download the repos, you will have nightly-build product.

If you download ['Release' section](https://github.com/dinhanhx/text-summarizer/releases), you will have stable product.

You can check out ['Wiki' section](https://github.com/dinhanhx/text-summarizer/wiki) to understand more about the backend and the frontend.
## 1. Requirements
```
pip install -r requirements.txt .
```
Run this command line in 'modules' folder to set up all packages.

```
python nltk_downloads.py
```
Run this command line in 'modules' folder to set up all components related to [nltk](https://www.nltk.org/).

## 2. Ignite the app
```
python text-sum-core.py
```
Run this command line in 'webapp' folder to start the application.

Open your favorite browser and go to this [link.](http://localhost:5000/text-summarizer)
```
http://localhost:5000/text-summarizer
```

## 3. Usage
It's quite easy to use.
### Plain text (in English)
You can paste your long text in the first input box then click summarize this.

The web app will return you as text file named out.txt
### Wikipedia article (in English)
You can paste a link to an English Wikipedia article such as [this](https://en.wikipedia.org/wiki/Loss_function) or [that](https://en.wikipedia.org/wiki/Communist_Party_of_Georgia_(Soviet_Union))
```
https://en.wikipedia.org/wiki/Communist_Party_of_Georgia_(Soviet_Union)
https://en.wikipedia.org/wiki/Loss_function
```
The web app will return you as text file named out.txt
### Documents (Purely created and in English)
You can upload a .pdf, .odt, .docx file then click summarize this.

The web app will return you as text file named out.txt

## 4. Some documents
You can check out in 'documents' folder.

[Software Requirements](https://docs.google.com/document/d/1JPUjkj7WB9qNS9bpn55QV00t1JlRpcWaTEJ1eBziqg0/)

[Software Design](https://docs.google.com/document/d/108BHsuCUpyInWNZPYqluplRkP0l9gAbkfa2SGPCXjkk/)

## 5. Videos
[March Update](https://youtu.be/UZ9a2ci0-4Q)

[April Update](https://youtu.be/4AlDmCvgi20)

[Mid April Update](https://youtu.be/qH50rilTa6E)

[Final Update]()

~ Author: Vu Dinh Anh ~
