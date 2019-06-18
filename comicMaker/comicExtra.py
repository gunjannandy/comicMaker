from .makeFullPdf import makeFullPdf
from .parseImage import parseImage
from .makePdf import makePdf
import requests,os,os.path,sys,time,json
from bs4 import BeautifulSoup

def comicExtra():
	while True:
		try:
			with open('config.json', 'r', encoding="utf-8") as f:
				books = json.load(f)
			library=[*books['comicExtra']]
			# print(library)
			# return
			if not library:
				# print("No books found!")
				return
			# print("List of books >")
			# for i in library:
			# 	print (" > '"+i+"' download will start from Chapter-"+books['comicExtra'][i])
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
		incompleteUrl="https://www.comicextra.com/comic/"+comicName+"/"
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
				# comicExtra()
				# return
			tryAgain=1
		chapterNames = []
		middleLinks = []
		totalChaptersToDownload = 0
		# soup.findAll("tbody",attrs={'id':'list'})
		
		# print(soup.findAll("tbody"))

		# for li in soup.findAll('li', attrs={'class':'wp-manga-chapter'}):
		for tr in soup.findAll('tbody', attrs={'id':'list'}):
			for td in tr.findAll('td'):
				for a in td.findAll('a'):
					middleLink=a['href'].split(comicName+"/")[1]
					ChapterName=middleLink.split("chapter-")[1]
					try:
						if float(ChapterName) >= float(books['comicExtra'][comicName]):
							chapterNames.append(ChapterName)
							middleLinks.append(middleLink)
							totalChaptersToDownload += 1
					except:
						chapterNames.append(ChapterName)
						middleLinks.append(middleLink)
						totalChaptersToDownload += 1

		middleLinks.reverse()
		chapterNames.reverse()
		# print(chapterNames)
		# print(middleLinks)
		# print(totalChaptersToDownload)
		# return
		parentDir=comicName+os.sep
		if os.path.exists(parentDir):
			print(comicName+" already exists.")
		else:
			os.makedirs(parentDir)
		print(" Opening "+comicName+" >")
		os.chdir(parentDir)
		if totalChaptersToDownload > 1 :
			countForMiddleLink=0
			for i in chapterNames:
				books['comicExtra'][comicName] = str(i)
				tryAgain=0
				while tryAgain==0:
					try:
						with open(originDirectory+os.sep+'config.json', 'w', encoding="utf-8") as file:
							json.dump(books, file, indent=4)
					except:
						continue
					tryAgain=1
				chapter="Chapter-"+i.replace('.','-')
				currentDir=chapter+os.sep
				# print(currentDir)
				# continue
				if os.path.exists(currentDir):
					print("  "+comicName+" > "+chapter+" already exists.")
				else:
					os.makedirs(currentDir)
				print("  Opening "+comicName+" > "+chapter+" > ("+str(totalChaptersToDownload)+" Remaining) >")
				os.chdir(currentDir)
				completeUrl=incompleteUrl.replace("comic/","")+middleLinks[countForMiddleLink]+"/full/"
				# print(completeUrl)
				# completeUrl=incompleteUrl+"chapter-"+i.replace('.','-')+"/"
				parseImage.comicExtra(completeUrl,chapter)
				# continue
				makePdf.comicExtra(chapter)
				os.chdir("..")
				countForMiddleLink+=1
				totalChaptersToDownload-=1
			makeFullPdf.comicExtra(comicName)
		else:
			print(" < "+comicName+" already fully downloaded.")
		os.chdir("..")
		print(" << Download finished of "+comicName+" <")
	os.chdir(originDirectory)
	return