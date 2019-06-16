import comicMaker,sys,json
# from multiprocessing import Process

sys.setrecursionlimit(25000)

def main():
	try:
		with open('config.json', 'r', encoding="utf-8") as f:
			books = json.load(f)
		mangaLikeLibrary=[*books['mangaLike']]
		readComicLibrary=[*books['readComic']]
		if not mangaLikeLibrary and not readComicLibrary:
			print("No books found!")
			return
		print("List of books >")
		if mangaLikeLibrary:
			for i in mangaLikeLibrary:
				print (" > '"+i+"' download will start from Chapter-"+books['mangaLike'][i])
		if readComicLibrary:
			for i in readComicLibrary:
				print (" > '"+i+"' download will start from Chapter-"+books['readComic'][i])
	except:
		# raise
	    print("No 'config.json' file found!")
	    return
	
	if not comicMaker.confirm():
		return

	# Process(target = comicMaker.mangaLike).start()
	# Process(target = comicMaker.readComic).start()
	comicMaker.mangaLike()
	comicMaker.readComic()
	print(" <<< All Downloads completed!")
	# return


if __name__ == '__main__':
	main()