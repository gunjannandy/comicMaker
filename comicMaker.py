import comicMaker
import requests,os,os.path,sys
from bs4 import BeautifulSoup

sys.setrecursionlimit(10000)

def main():
	try:
	    with open("links.txt", "r", encoding="utf-8") as f:
	        library = []
	        print("List of books >")
	        for line in f:
	            if (line[0:1]=='#' or line[0:1]=='\n'):
	                continue
	            list_of_words = line.split('/')
	            book=(list_of_words[list_of_words.index("mangalike.net") + 2])
	            print("    > "+book)
	            library.append(book)
	        if not library:
	            print("No books found!")
	            return
	except:
	    print("No 'links.txt' file found!")
	    return
	
	if not comicMaker.confirm():
		return
	os.chdir('..')
	os.chdir('comicDownloads\\')
	for comicName in library:
		incompleteUrl="https://mangalike.net/manga/"+comicName+"/"

		page_response = requests.get(incompleteUrl, timeout=5)
		soup = BeautifulSoup(page_response.content, "html.parser")
		chapterNum=[]
		for li in soup.findAll('li', attrs={'class':'wp-manga-chapter'}):
			string=li.find('a').contents[0]
			list_of_words = string.split( )
			chapterNum.append(list_of_words[list_of_words.index("Chapter") + 1])
		chapterNum.reverse()
		parentDir=comicName+"/"
		if os.path.exists(parentDir):
			print(comicName+" already exists.")
		else:
			os.makedirs(parentDir)
		print(" Opening "+comicName+" >")
		os.chdir(parentDir)

		for i in chapterNum:
			# use the below lines to start execution to a selected chapter
			#if comicName=="girl-and-science" and (float(i)<23):
			#	continue
			chapter="Chapter-"+i.replace('.','-')
			currentDir=chapter+"/"
			if os.path.exists(currentDir):
				print("  "+comicName+" > "+chapter+" already exists.")
			else:
				os.makedirs(currentDir)
			print("  Opening "+comicName+" > "+chapter+" >")
			os.chdir(currentDir)
			completeUrl=incompleteUrl+"chapter-"+i.replace('.','-')+"/"
			comicMaker.parseImage(completeUrl,chapter)
			comicMaker.makePdf(chapter)
			os.chdir("..")
		comicMaker.makeFullPdf(comicName)
		os.chdir("..")
		print(" Download finished of "+comicName+" <")
	print(" > All Downloads completed!")


if __name__ == '__main__':
	main()