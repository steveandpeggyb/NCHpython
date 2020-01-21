import PyPDF2

pdfFileObj = open('./PDF/Automate.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print('Number of Pages: ' + str(pdfReader.numPages))

pageObj = pdfReader.getPage(320)  #   zero base pages.  So, page zero (0) is actually page one (1)
print(pageObj.extractText())