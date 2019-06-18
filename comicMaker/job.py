from .saveImage import saveImage

class job:

	def mangaLike(url,chapter):
		for img in url:
	 		link = img['src']
	 		pageNum = img['id'].replace('ima','pa')
	 		saveImage(link,chapter,pageNum)

	def readComicOnlineTo(url,chapter,pageNum):
 		saveImage(url,chapter,pageNum)

	def readComicsOnlineRu(url,chapter,pageNum):
		saveImage(url,chapter,pageNum)

	def comicExtra(url,chapter,pageNum):
		saveImage(url,chapter,pageNum)