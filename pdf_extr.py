from PyPDF2 import PdfReader

reader = PdfReader("shag.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"
vals = []
for i in text.split("\n"):
    for b in i.split(". "):
        if len(b) >= 3:
            vals.append(b)
print(vals[0])
