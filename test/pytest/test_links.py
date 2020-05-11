from abberivator_flow import wikipedia_abberivator as wa

fobj = open('../case/links.txt', 'r', encoding = 'utf8')
links = fobj.readlines()
fobj.close()
links = [link.rstrip() for link in links]

pairs = []
for link in links:
    output_str = wa.summarize(link)
    pairs.append((output_str, ''))

import pytest
@pytest.mark.parametrize(('x', 'y'), pairs)
def test_pairs(x, y):
    assert x != y
