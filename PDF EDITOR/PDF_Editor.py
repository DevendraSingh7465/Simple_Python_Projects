# Module Used - PyPDF2
# operations - mearge PDF 
from PyPDF2 import PdfMerger
import os
print('''
Put all PDF files in one Folder than copy Folder Location and paste below.
it will automatically merge all the PDF files present in the folder.
''')
source = input("Enter PDF Folder location : ")
source = source + "\\"
source.replace('\\','/')
pdf_files = os.listdir(source)
pdf_file_names = []

print(f"PDF Files Present in Folder are : ", end=" ")
for file in pdf_files:
    if file.endswith('.pdf'):
        print(file,end=" , ")
        name = source + file
        pdf_file_names.append(name)
print()

os.chdir(source) # change directory to save new PDF file in the same location

newpdf = PdfMerger() # create new PDF file
for i in range(len(pdf_file_names)):
    files = open(pdf_file_names[i],'rb')
    newpdf.append(files) # adds pdf file one by one in new pdf
savePDF = input("Enter file name to save merged files : ")
if savePDF.endswith(".pdf"):
    pass
else:
    savePDF = savePDF + ".pdf"
newpdf.write(savePDF) # save PDF

print(f"New PDF File Location : {source}{savePDF}")
