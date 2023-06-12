from PyPDF2 import PdfReader
from invoice2data import extract_data
from invoice2data.extract.loader import read_templates
import os
import csv

pdf_path = 'pdfs/'
templates = read_templates('C:/Users/your_username/anaconda3/Lib/site-packages/invoice2data/extract/templates/')
fhand = open('error_logs.txt','w')

headers = ['filename','issuer', 'invoice_number', 'date', 'amount', 'currency', 'desc']

with open('output.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()

    for filename in os.listdir(pdf_path):
        if os.path.isfile(os.path.join(pdf_path, filename)) and os.path.splitext(filename)[1].lower() == ".pdf":
            text = "" 
            filepath = pdf_path + filename
            reader = PdfReader(filepath) 
            print(filename,"has ",len(reader.pages),"pages")
            for i in range(len(reader.pages)):
                page = reader.pages[i]
                text = text+page.extract_text()
            fp = open('asdf;lkj.txt','w')
            fp.write(text)
            fp.close()
            try:
                result = extract_data('asdf;lkj.txt', templates=templates)
                print(result)
                buf=result
                buf["filename"]=filename
                # result['filename']=filename
                writer.writerow(buf)
            except Exception as e:
                fhand.write(filename + " " + str(e) + "\n")
                
fhand.close()
