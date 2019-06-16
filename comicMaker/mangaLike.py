from .makeFullPdf import makeFullPdf
from .parseImage import parseImage
from .makePdf import makePdf
from .confirm import confirm
import requests,os,os.path,sys,time,json
from bs4 import BeautifulSoup

def mangaLike():
	try:
		with open('config.json', 'r', encoding="utf-8") as f:
			books = json.load(f)
		library=[*books['mangaLike']]
		# print(library)
		# return
		if not library:
			print("No books found!")
			return
		print("List of books >")
		for i in library:
			print (" > '"+i+"' download will start from Chapter-"+books['mangaLike'][i])
	except:
		# raise	    print("No 'config.json' file found!")
	    return
	
	if not confirm():
		return
	originDirectory=os.getcwd()
	os.chdir('..')
	os.chdir('comicDownloads'+os.sep)
	for comicName in library:
		incompleteUrl="https://mangalike.net/manga/"+comicName+"/"
		try:
			page_response = requests.get(incompleteUrl, timeout=5)
			soup = BeautifulSoup(page_response.content, "html.parser")
		except:
			print("Could not connect, trying again in 5 seconds!")
			time.sleep(5)
			os.chdir('..')
			os.chdir('comicMaker'+os.sep)
			mangaLike()
			return

		chapterNum = []
		totalChaptersToDownload = 0
		for li in soup.findAll('li', attrs={'class':'wp-manga-chapter'}):
			string=li.find('a').contents[0]
			list_of_words = string.split( )
			validChapterNum = list_of_words[list_of_words.index("Chapter") + 1]
			if float(validChapterNum) >= float(books['mangaLike'][comicName]):
				chapterNum.append(validChapterNum)
				totalChaptersToDownload += 1
		chapterNum.reverse()
		parentDir=comicName+"/"
		if os.path.exists(parentDir):
			print(comicName+" already exists.")
		else:
			os.makedirs(parentDir)
		print(" Opening "+comicName+" >")
		os.chdir(parentDir)
		if totalChaptersToDownload > 1 :
			for i in chapterNum:
				books['mangaLike'][comicName] = str(i)
				with open(originDirectory+os.sep+'config.json', 'w', encoding="utf-8") as file:
					json.dump(books, file, indent=4)
				chapter="Chapter-"+i.replace('.','-')
				currentDir=chapter+"/"
				if os.path.exists(currentDir):
					print("  "+comicName+" > "+chapter+" already exists.")
				else:
					os.makedirs(currentDir)
				print("  Opening "+comicName+" > "+chapter+" >")
				os.chdir(currentDir)
				completeUrl=incompleteUrl+"chapter-"+i.replace('.','-')+"/"
				parseImage.mangaLike(completeUrl,chapter)
				makePdf.mangaLike(chapter)
				os.chdir("..")
			makeFullPdf.mangaLike(comicName)
		else:
			print(" < "+comicName+" already fully downloaded.")
		os.chdir("..")
		print(" << Download finished of "+comicName+" <")
	print(" <<< All Downloads completed!")
	os.chdir(originDirectory)
	return