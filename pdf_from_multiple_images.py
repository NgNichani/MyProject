import os
from fpdf import FPDF
pdf = FPDF()
# imagelist is the list with all image filenames

foldername = 'foldername'
img_path = 'XXXX'

mydict = {}
for i in os.listdir(img_path):
    if i.endswith(".png"):
        # mydict[i]=int(i.split('.')[0])
        mydict[int(i.split('.')[0])] = i

print(sorted(mydict.keys(), key=int))

for image in sorted(mydict.keys(), key=int):
    pdf.add_page()
    pdf.image(img_path + mydict[image], 0, 0, 210, 210)
pdf.output(img_path + foldername + ".pdf", "F")
