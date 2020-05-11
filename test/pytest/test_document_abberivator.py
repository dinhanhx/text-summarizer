def test_pdf():
    from abberivator_flow import document_abberivator as da
    assert da.summarize('../case/sample1/sample1.pdf') != ''

def test_odt():
    from abberivator_flow import document_abberivator as da
    assert da.summarize('../case/sample1/sample1.odt') != ''

def test_docx():
    from abberivator_flow import document_abberivator as da
    assert da.summarize('../case/sample1/sample1.docx') != ''
