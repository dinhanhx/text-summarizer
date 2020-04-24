def test_output():
    from abberivator_flow import scriptum_abberivator as sa
    fobj = open('../case/sample1/sample1.txt', 'r', encoding = 'utf8')
    text = fobj.read()
    fobj.close()
    assert sa.summarize(text) != ''
