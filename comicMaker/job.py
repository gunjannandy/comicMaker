from .saveImage import saveImage

def job(url,chapter):
	for img in url:
 		link = img['src']
 		pageNum = img['id'].replace('ima','pa')
 		saveImage(link,chapter,pageNum)