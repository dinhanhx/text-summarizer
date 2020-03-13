import scriptum_abberivator as sa

text_file = open('A_long_text.txt', 'r')
text = text_file.read()
text_file.close()

text_sum = sa.summary(text)

print(text_sum)