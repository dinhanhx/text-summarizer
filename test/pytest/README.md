## Use what to test?
[PyTest](https://docs.pytest.org/en/latest/)

Installation `pip install pytest`

Usage `pytest test_sample.py`

## What to test?
```Python
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

## Use what sample?
'test/case' folder
