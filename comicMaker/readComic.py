from .makeFullPdf import makeFullPdf
from .parseImage import parseImage
from .rotateProxy import rotateProxy
from .checkInternet import checkInternet
from .makePdf import makePdf
import requests,os,os.path,sys,time,json,cfscrape
from bs4 import BeautifulSoup

def readComic():
	while True:
		try:
			with open('config.json', 'r', encoding="utf-8") as f:
				books = json.load(f)
			library=[*books['readComic']]
			if not library:
				# print("No books found!")
				return
			# print("List of books >")
			# for i in library:
			# 	print (" > '"+i+"' download will start from Chapter-"+books['readComic'][i])
		except:
			# raise
		    # print("No 'config.json' file found!")
		    # return
		    continue
		break
	# if not confirm():
	# 	return

	originalWorkingDirectory=os.getcwd()
	os.chdir('..')
	if not os.path.exists('comicDownloads'+os.sep):
		os.makedirs('comicDownloads'+os.sep)
	os.chdir('comicDownloads'+os.sep)
	proxyNumber=0
	proxyCount=0
	while proxyCount<5:
		proxyList=rotateProxy.createProxyList("https://readcomiconline.to/Comic/")
		# proxyList=rotateProxy.createProxyList("https://google.com/")
		proxyCount=len(proxyList)
	
	for comicName in library:
		incompleteUrl="https://readcomiconline.to/Comic/"+comicName+"/"
		tryAgain=0
		while tryAgain == 0:
			try:
				if not checkInternet():
					print("Could not connect, trying again in 3 seconds!")
					time.sleep(3)
					os.chdir(originalWorkingDirectory)
					readComic()
					return
				
				scraper = cfscrape.create_scraper()
				# requests.packages.urllib3.disable_warnings()
				# nonstrcfurl = scraper.get(incompleteUrl,proxies={"http": proxyList[proxyNumber], "https": proxyList[proxyNumber]},headers={'User-Agent': 'Chrome'}, timeout=20).content
				print("    Trying with : "+proxyList[proxyNumber])
				nonstrcfurl = scraper.get(incompleteUrl,proxies={"https": proxyList[proxyNumber]},headers={'User-Agent': 'Chrome'}, timeout=20).content
				cfurl = str(nonstrcfurl)

				# with open(originalWorkingDirectory+os.sep+"cfurl.txt","wb") as f:
				# 	f.write(nonstrcfurl)
				# print(cfurl)
				# return

			except:
				# raise
				print("     Proxy went down..trying again...")
				proxyNumber=(proxyNumber+1)%len(proxyList)
				continue
				# os.chdir(originalWorkingDirectory)
				# readComic()
				# return
			tryAgain=1 #for breaking the while loop
		# for i in range(1,100): print(i)
		chapterNames = []
		middleLink = []
		totalChaptersToDownload = 0
		# print(cfurl)
		# print(cfurl.count("href=\"/Comic/"+comicName+"/"))
		for i in range(1,cfurl.count("href=\"/Comic/"+comicName+"/")+1):
			# print(cfurl)
			firstSplit=(cfurl.split("href=\"/Comic/"+comicName+"/")[i])
			middleSplit=firstSplit.split("\"")[0]
			finalSplit=middleSplit.split("?id=")[0]
			# print(firstSplit)
			# print(middleSplit)
			# print(finalSplit)
			# print(finalSplit.split("-")[1])
			# continue
			# if (finalSplit == "Full"):
			# 	middleLink.append(middleSplit)
			# 	chapterNames.append(finalSplit)
			# 	totalChaptersToDownload += 1
			# 	fullComicFlag = 1
			try:
				if float(finalSplit.split("-")[1]) >= float(books['readComic'][comicName]):
					middleLink.append(middleSplit)
					chapterNames.append(finalSplit)
					totalChaptersToDownload += 1
			except:
				middleLink.append(middleSplit)
				chapterNames.append(finalSplit)
				totalChaptersToDownload += 1
		# continue
		# print(chapterNames)
		# return
		chapterNames.reverse()
		middleLink.reverse()
		parentDir=comicName+"/"
		if os.path.exists(parentDir):
			print(comicName+" already exists.")
		else:
			os.makedirs(parentDir)
		print(" Opening "+comicName+" >")
		pagesCrawledWithSameProxy = 0
		os.chdir(parentDir)
		if totalChaptersToDownload > 0 :
			countForMiddleLink=0
			for i in chapterNames:
				if pagesCrawledWithSameProxy > 50:
					proxyNumber=(proxyNumber+1)%len(proxyList)
					print("Changing proxy...Before getting banned...")
					print("Trying with : "+proxyList[proxyNumber])
					pagesCrawledWithSameProxy = 0
				# print(str(i).split("-")[1])
				# continue
				try:
					books['readComic'][comicName] = str(i).split("-")[1]
				except:
					pass
				tryAgain=0
				while tryAgain==0:
					try:
						with open(originalWorkingDirectory+os.sep+'config.json', 'w', encoding="utf-8") as file:
							json.dump(books, file, indent=4)
					except:
						continue
					tryAgain=1
				# chapter="Chapter-"+i.replace('.','-')
				chapter = str(i)
				currentDir=chapter+"/"
				if os.path.exists(currentDir):
					print("  "+comicName+" > "+chapter+" already exists.")
				else:
					os.makedirs(currentDir)
				print("  Opening "+comicName+" > "+chapter+" >")
				os.chdir(currentDir)
				completeUrl=incompleteUrl+middleLink[countForMiddleLink]+"&readType=1&quality=hq"
				print("   Fooling Cloudflare...")
				parseImage.readComic(completeUrl,chapter,proxyList,proxyNumber)
				makePdf.readComic(chapter)
				os.chdir("..")
				pagesCrawledWithSameProxy+=1
				countForMiddleLink+=1
			makeFullPdf.readComic(comicName)
		else:
			print(" < "+comicName+" already fully downloaded.")
		os.chdir("..")
		print(" << Download finished of "+comicName+" <")
	os.chdir(originalWorkingDirectory)
	return