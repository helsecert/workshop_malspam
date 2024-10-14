with open('Document.pdf.lnk','rb') as f:
    fil = f.read()
with open("stage2",'wb') as f:
    f.write(fil[4901:])

