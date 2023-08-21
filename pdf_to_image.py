from pdf2image import convert_from_path
from datetime import date 

# Get current Date
current_date=date.today().strftime(("%d_%b_%Y"))

# File path with directory path and current date
directory_path = r"D:\Testing\power_bi\output"
pdf_file_path= f"{directory_path}\{current_date}_PowerBi_Dashboard.pdf"

print(pdf_file_path)
old_pdf= convert_from_path(pdf_file_path,
                          poppler_path=r"D:\Testing\power_bi\poppler-23.08.0\Library\bin")

for i in range(len(old_pdf)):
    old_pdf[i].save(f"{directory_path}\PB_"+str(i)+".jpg","JPEG")
