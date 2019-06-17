from .makeFullPdf import makeFullPdf
from .parseImage import parseImage
from .makePdf import makePdf
import requests,os,os.path,sys,time,json
from bs4 import BeautifulSoup

def readComicsOnlineRu():
	while True:
		try:
			with open('config.json', 'r', encoding="utf-8") as f:
				books = json.load(f)
			library=[*books['readComicsOnlineRu']]
			# print(library)
			# return
			if not library:
				# print("No books found!")
				return
			# print("List of books >")
			# for i in library:
			# 	print (" > '"+i+"' download will start from Chapter-"+books['readComicsOnlineRu'][i])
		except:
			# raise	    
			# print("No 'config.json' file found!")
			# return
			continue
		break
	
	# if not confirm():
	# 	return
	originDirectory=os.getcwd()
	os.chdir('..')
	if not os.path.exists('comicDownloads'+os.sep):
		os.makedirs('comicDownloads'+os.sep)
	os.chdir('comicDownloads'+os.sep)
	for comicName in library:
		incompleteUrl="https://readcomicsonline.ru/comic/"+comicName+"/"
		tryAgain=0
		while tryAgain==0:
			try:
				page_response = requests.get(incompleteUrl, timeout=5)
				soup = BeautifulSoup(page_response.content, "html.parser")
			except:
				print("Could not connect, trying again in 5 seconds!")
				time.sleep(5)
				continue
				# os.chdir('..')
				# os.chdir('comicMaker'+os.sep)
				# readComicsOnlineRu()
				# return
			tryAgain=1
		chapterNum = []
		totalChaptersToDownload = 0

		for li in soup.findAll('li', attrs={'class':'volume-0'}):
			# validChapterNum=li.find('a').contents[0].split("#")[1]
			validChapterNum=li.find('a')['href'].split(comicName+"/")[1]
			try:
				if float(validChapterNum) >= float(books['readComicsOnlineRu'][comicName]):
					chapterNum.append(validChapterNum)
					totalChaptersToDownload += 1
			except:
				chapterNum.append(validChapterNum)
				totalChaptersToDownload += 1
		chapterNum.reverse()
		# print(chapterNum)
		# return
		parentDir=comicName+os.sep
		if os.path.exists(parentDir):
			print(comicName+" already exists.")
		else:
			os.makedirs(parentDir)
		print(" Opening "+comicName+" >")
		os.chdir(parentDir)
		if totalChaptersToDownload > 1 :
			for i in chapterNum:
				books['readComicsOnlineRu'][comicName] = str(i)
				tryAgain=0
				while tryAgain==0:
					try:
						with open(originDirectory+os.sep+'config.json', 'w', encoding="utf-8") as file:
							json.dump(books, file, indent=4)
					except:
						continue
					tryAgain=1
				chapter=i
				currentDir=chapter.replace('.','-')+os.sep
				if os.path.exists(currentDir):
					print("  "+comicName+" > "+chapter.replace('.','-')+" already exists.")
				else:
					os.makedirs(currentDir)
				print("  Opening "+comicName+" > "+chapter+" > ("+str(totalChaptersToDownload)+" Remaining) >")
				os.chdir(currentDir)
				completeUrl=incompleteUrl+i+"/"
				parseImage.readComicsOnlineRu(comicName,completeUrl,chapter)
				makePdf.readComicsOnlineRu(chapter)
				os.chdir("..")
				totalChaptersToDownload -= 1
			makeFullPdf.readComicsOnlineRu(comicName)
		else:
			print(" < "+comicName+" already fully downloaded.")
		os.chdir("..")
		print(" << Download finished of "+comicName+" <")
	os.chdir(originDirectory)
	return