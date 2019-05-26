import shutil,os,os.path
from PyPDF2 import PdfFileMerger

def makeFullPdf(comicBook):
	print("    Merging all pdf's, please wait!")
	for file in os.listdir("."):
	    if file.endswith(".pdf"):
	        os.remove(os.path.join(".", file))
	pdflist=[]
	for dirpath, dirnames, filenames in os.walk('.'):
	    for filename in [f for f in filenames if f.endswith(".pdf")]:
	        address=os.path.join(dirpath, filename)
	        if os.stat(address).st_size!=0:
	        	pdflist.append(filename)
		        #print(address)
		        shutil.copy( address, '.')
	try:
		sortedpdf=[]
		sortedlist=[]
		for i in pdflist:
		    temp=float((i[i.find("Chapter-")+8 : i.find(".pdf")]).replace('-','.'))
		    sortedlist.append(temp)
		sortedlist.sort()
		for i in sortedlist:
		    sortedpdf.append("Chapter"+"-"+((str(i)).replace('.','-')).replace('-0','')+".pdf")
		#print(sortedpdf)
		merger = PdfFileMerger()
		for pdf in sortedpdf:
		    merger.append(pdf)

		fd = None
		try:
		    fd = open(comicBook+".pdf", 'wb')
		    merger.write(fd)
		finally:
			fd.close()
			merger.close()

		for pdf in sortedpdf:
		    os.remove(pdf)
		print("    "+comicBook+".pdf saved!")
	except:
		print("    Error while creating"+comicBook+"!")
		if os.path.exists(comicBook+".pdf"):
			os.remove(comicBook+".pdf")
