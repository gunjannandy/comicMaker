from .saveImage import saveImage

class job:

	def mangaLike(url,chapter):
		for img in url:
	 		link = img['src']
	 		pageNum = img['id'].replace('ima','pa')
	 		saveImage.mangaLike(link,chapter,pageNum)

	def readComic(url,chapter,pageNum):
 		# pageNum = (url.split("/RCO")[1]).split(".jpg")[0]
 		saveImage.readComic(url,chapter,pageNum)