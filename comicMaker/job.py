from .saveImage import saveImage

class job:

	def mangaLike(url,chapter):
		for img in url:
	 		link = img['src']
	 		pageNum = img['id'].replace('ima','pa')
	 		saveImage.mangaLike(link,chapter,pageNum)

	def readComicOnlineTo(url,chapter,pageNum):
 		saveImage.readComicOnlineTo(url,chapter,pageNum)

	def readComicsOnlineRu(url,chapter,pageNum):
		saveImage.readComicsOnlineRu(url,chapter,pageNum)