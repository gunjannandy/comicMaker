from .makeFullPdf import makeFullPdf
from .parseImage import parseImage
from .makePdf import makePdf
from .confirm import confirm
import requests,os,os.path,sys,time,json,cfscrape
from bs4 import BeautifulSoup

def readComic():
	try:
		with open('config.json', 'r', encoding="utf-8") as f:
			books = json.load(f)
		library=[*books['readComic']]
		if not library:
			print("No books found!")
			return
		print("List of books >")
		for i in library:
			print (" > '"+i+"' download will start from Chapter-"+books['readComic'][i])
	except:
		# raise
	    print("No 'config.json' file found!")
	    return
	
	if not confirm():
		return

	originDirectory=os.getcwd()
	os.chdir('..')
	os.chdir('comicDownloads'+os.sep)
	for comicName in library:
		incompleteUrl="https://readcomiconline.to/Comic/"+comicName+"/"
		try:
			scraper = cfscrape.create_scraper()
			nonstrcfurl = scraper.get(incompleteUrl).content
			cfurl = str(nonstrcfurl)
			# page_response = requests.get(incompleteUrl, timeout=5)
			# soup = BeautifulSoup(page_response.content, "html.parser")
		except:
			print("Could not connect, trying again in 5 seconds!")
			time.sleep(5)
			os.chdir('..')
			os.chdir('comicMaker'+os.sep)
			readComic()

		chapterNames = []
		middleLink = []
		totalChaptersToDownload = 0
		for i in range(1,cfurl.count("<a  href=\"/Comic/"+comicName+"/")+1):

			firstSplit=(cfurl.split("<a  href=\"/Comic/"+comicName+"/")[i])
			middleSplit=firstSplit.split("\"")[0]
			finalSplit=middleSplit.split("?id=")[0]
			
			if float(finalSplit.split("-")[1]) >= float(books['readComic'][comicName]):
				middleLink.append(middleSplit)
				chapterNames.append(finalSplit)
				totalChaptersToDownload += 1
		# print(chapterNames)
		# continue
		chapterNames.reverse()
		middleLink.reverse()
		parentDir=comicName+"/"
		if os.path.exists(parentDir):
			print(comicName+" already exists.")
		else:
			os.makedirs(parentDir)
		print(" Opening "+comicName+" >")
		os.chdir(parentDir)
		if totalChaptersToDownload > 1 :
			count=0
			for i in chapterNames:
				# print(str(i).split("-")[1])
				# continue
				books['readComic'][comicName] = str(i).split("-")[1]
				with open(originDirectory+os.sep+'config.json', 'w', encoding="utf-8") as file:
					json.dump(books, file, indent=4)
				# chapter="Chapter-"+i.replace('.','-')
				chapter = str(i)
				currentDir=chapter+"/"
				if os.path.exists(currentDir):
					print("  "+comicName+" > "+chapter+" already exists.")
				else:
					os.makedirs(currentDir)
				print("  Opening "+comicName+" > "+chapter+" >")
				os.chdir(currentDir)
				completeUrl=incompleteUrl+middleLink[count]+"&readType=1&quality=hq"
				print("   Fooling Cloudflare...")
				parseImage.readComic(completeUrl,chapter)
				makePdf.readComic(chapter)
				os.chdir("..")
				count+=1
			makeFullPdf.readComic(comicName)
		else:
			print(" < "+comicName+" already fully downloaded.")
		os.chdir("..")
		print(" << Download finished of "+comicName+" <")
	print(" <<< All Downloads completed!")
	os.chdir(originDirectory)