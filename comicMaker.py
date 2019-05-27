import comicMaker
import requests,os,os.path,sys,time
from bs4 import BeautifulSoup
import json

sys.setrecursionlimit(25000)

def main():
	try:
		with open('config.json', 'r', encoding="utf-8") as f:
			books = json.load(f)
		library=[*books]
		if not library:
			print("No books found!")
			return
		print("List of books >")
		for i in library:
			print (" > '"+i+"' download will start from Chapter-"+books[i])
	except:
		#raise
	    print("No 'config.json' file found!")
	    return
	
	if not comicMaker.confirm():
		return
	originDirectory=os.getcwd()
	os.chdir('..')
	os.chdir('comicDownloads\\')
	for comicName in library:
		incompleteUrl="https://mangalike.net/manga/"+comicName+"/"
		try:
			page_response = requests.get(incompleteUrl, timeout=5)
			soup = BeautifulSoup(page_response.content, "html.parser")
		except:
			print("Could not connect, trying again in 5 seconds!")
			time.sleep(5)
			os.chdir('..')
			os.chdir('comicMaker\\')
			main()

		chapterNum=[]
		for li in soup.findAll('li', attrs={'class':'wp-manga-chapter'}):
			string=li.find('a').contents[0]
			list_of_words = string.split( )
			validChapterNum = list_of_words[list_of_words.index("Chapter") + 1]
			if float(validChapterNum) >= float(books[comicName]):
				chapterNum.append(validChapterNum)
		chapterNum.reverse()
		parentDir=comicName+"/"
		if os.path.exists(parentDir):
			print(comicName+" already exists.")
		else:
			os.makedirs(parentDir)
		print(" Opening "+comicName+" >")
		os.chdir(parentDir)

		for i in chapterNum:
			books[comicName] = str(i)
			with open(originDirectory+'\\config.json', 'w', encoding="utf-8") as file:
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
			comicMaker.parseImage(completeUrl,chapter)
			comicMaker.makePdf(chapter)
			os.chdir("..")
		comicMaker.makeFullPdf(comicName)
		os.chdir("..")
		print(" Download finished of "+comicName+" <")
	print(" > All Downloads completed!")


if __name__ == '__main__':
	main()