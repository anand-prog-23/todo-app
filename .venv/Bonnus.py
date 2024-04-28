filenames=['doc.txt','report.txt','presentation.tx']

for i in filenames:
    newfile=open(i,'w')
    newfile.write("Hello\n")
    newfile.write('Hello1')
    newfile.close()