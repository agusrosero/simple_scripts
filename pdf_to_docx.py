# Convertir de PDF a DOCX
from pdf2docx import Converter

pdf_file = "PATH/TO/PDF"
docx_file = "final.docx"

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()
