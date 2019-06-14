import os,requests,itertools,cfscrape
from bs4 import BeautifulSoup
import multiprocessing as mp
from multiprocessing.dummy import Pool
from .job import job
from .saveImage import saveImage

class parseImage:

	def mangaLike(url,chapter):
		try:
			page_response = requests.get(url, timeout=10)
			soup = BeautifulSoup(page_response.content, "html.parser")
		except:
			print("Could not connect, Trying again!")
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

	def readComic(url,chapter):
		try:
			scraper = cfscrape.create_scraper()
			nonstrcfurl = scraper.get(url).content
			cfurl = str(nonstrcfurl)
		except:
			print("Could not connect, Trying again!")
			parseImage.readComic(url,chapter)
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

			# if (threading < 0):
			# 	print("  Bursting is not possible, starting iteration...")
			# 	for i in range (1,linkCount+1):
			# 		pageNum="%03d"%i
			# 		saveImage.readComic(links[i-1],chapter,pageNum)
			
			# elif (threading > -1):
			# 	if linkCount > 90:
			# 		linkCount = 90
			# 	elif linkCount < 2*mp.cpu_count():
			# 		linkCount = 2*mp.cpu_count()
			# 	print("  Starting burst engine...")
			# 	with Pool(processes=linkCount) as pool:
			# 		pool.starmap(job.readComic, zip(links, itertools.repeat(chapter)))
			
			for i in range (1,linkCount+1):
				pageNum.append("%03d"%i)
			if linkCount > 90:
				linkCount = 90
			elif linkCount < 2*mp.cpu_count():
				linkCount = 2*mp.cpu_count()
			print("  Starting burst engine...")
			with Pool(processes=linkCount) as pool:
				pool.starmap(job.readComic, zip(links, itertools.repeat(chapter), pageNum))
