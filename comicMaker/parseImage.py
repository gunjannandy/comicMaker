import os,requests,itertools,cfscrape,time
from bs4 import BeautifulSoup
import multiprocessing as mp
from multiprocessing.dummy import Pool
from .job import job
from .saveImage import saveImage
from .checkInternet import checkInternet
from .rotateProxy import rotateProxy

class parseImage:

	def mangaLike(url,chapter):
		try:
			page_response = requests.get(url, timeout=10)
			soup = BeautifulSoup(page_response.content, "html.parser")
		except:
			print("Could not connect, trying again in 5 seconds!")
			time.sleep(5)
			parseImage.mangaLike(url,chapter)
			return
		else:
			data = soup.findAll('div',attrs={'class':"page-break"})
			links=[]
			for div in data:
				links.append(div.findAll('img'))
			# linkCount = 2*mp.cpu_count() - 1
			linkCount=0
			for i in links:
				linkCount+=1
			if linkCount > 90:
				linkCount = 90
			elif linkCount < 2*mp.cpu_count():
				linkCount = 2*mp.cpu_count()
			print("  Starting burst engine...")
			with Pool(processes=linkCount) as pool:
				pool.starmap(job.mangaLike, zip(links, itertools.repeat(chapter)))

	def readComic(url,chapter,proxyList,proxyNumber):
		try:
			if not checkInternet():
				print("Could not connect, trying again in 5 seconds!")
				time.sleep(5)
				parseImage.readComic(url,chapter,proxyList,proxyNumber)
				return
			# proxy=rotateProxy()
			scraper = cfscrape.create_scraper()
			# requests.packages.urllib3.disable_warnings()
			# nonstrcfurl = scraper.get(url,proxies={"http": proxyList[proxyNumber], "https": proxyList[proxyNumber]}, headers={'User-Agent': 'Chrome'}).content
			print("    Trying with : "+proxyList[proxyNumber])
			nonstrcfurl = scraper.get(url,proxies={"https": proxyList[proxyNumber]}, headers={'User-Agent': 'Chrome'}).content
			# nonstrcfurl = scraper.get(url).content
			cfurl = str(nonstrcfurl)
		except:
			print("     Proxy went down..Changing proxy...")
			proxyNumber=(proxyNumber+1)%len(proxyList)
			print("    Trying with : "+proxyList[proxyNumber])
			parseImage.readComic(url,chapter,proxyList,proxyNumber)
			return
		
			# cfurl = str(nonstrcfurl)
			# open("read.txt",'wb').write(nonstrcfurl)
		else:
			links=[]
			pageNum=[]
			linkCount=0

			for i in range(1,cfurl.count("lstImages.push(\"")+1):
				firstSplit=(cfurl.split("lstImages.push(\"")[i])
				finalSplit=firstSplit.split("\")")[0]
				links.append(finalSplit)
				linkCount+=1
			
			for i in range (1,linkCount+1):
				pageNum.append("%03d"%i)
			if linkCount > 90:
				linkCount = 90
			elif linkCount < 2*mp.cpu_count():
				linkCount = 2*mp.cpu_count()
			print("  Starting burst engine...")
			with Pool(processes=linkCount) as pool:
				pool.starmap(job.readComic, zip(links, itertools.repeat(chapter), pageNum))
