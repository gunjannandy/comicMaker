import os,requests,itertools
from bs4 import BeautifulSoup
import multiprocessing as mp
from multiprocessing.dummy import Pool
from .job import job

def parseImage(url,chapter):
	try:
		page_response = requests.get(url, timeout=10)
		soup = BeautifulSoup(page_response.content, "html.parser")
	except:
		print("Could not connect, Trying again!")
		parseImage(url,chapter)
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
			pool.starmap(job, zip(links, itertools.repeat(chapter)))