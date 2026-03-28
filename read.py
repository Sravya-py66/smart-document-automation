import PyPDF2

# Open the REAL pdf
file = open('sample.pdf', 'rb')
reader = PyPDF2.PdfReader(file)

# Just get the first page to test
page = reader.pages[0]
text = page.extract_text()

print("Extracted Text:")
print(text)

file.close()