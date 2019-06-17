import comicMaker,sys,json
# from multiprocessing import Process

sys.setrecursionlimit(25000)

def main():
	try:
		with open('config.json', 'r', encoding="utf-8") as f:
			books = json.load(f)
		mangaLikeLibrary=[*books['mangaLike']]
		readComicOnlineToLibrary=[*books['readComicOnlineTo']]
		readComicsOnlineRuLibrary=[*books['readComicsOnlineRu']]
		if not mangaLikeLibrary and not readComicOnlineToLibrary and not readComicsOnlineRuLibrary:
			print("No books found!")
			return
		print("List of books >")
		if mangaLikeLibrary:
			for i in mangaLikeLibrary:
				print (" > '"+i+"' download will start from Chapter-"+books['mangaLike'][i])
		if readComicOnlineToLibrary:
			for i in readComicOnlineToLibrary:
				print (" > '"+i+"' download will start from Chapter-"+books['readComicOnlineTo'][i])
		if readComicsOnlineRuLibrary:
			for i in readComicsOnlineRuLibrary:
				print (" > '"+i+"' download will start from Chapter-"+books['readComicsOnlineRu'][i])
	except:
		# raise
	    print("No 'config.json' file found!")
	    return
	
	# if not comicMaker.confirm():
		# return

	# Process(target = comicMaker.mangaLike).start()
	# Process(target = comicMaker.readComicOnlineTo).start()
	comicMaker.mangaLike()
	comicMaker.readComicOnlineTo()
	comicMaker.readComicsOnlineRu()
	print(" <<< All Downloads completed!")
	# return


if __name__ == '__main__':
	main()
