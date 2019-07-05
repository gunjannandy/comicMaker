import comicMaker,sys,json
# from multiprocessing import Process

sys.setrecursionlimit(25000)

def main():
	# printing comicMaker logo
	with open('asciiLogo.txt') as f:
		asciiLogo=f.read()
		print(asciiLogo)
	try:
		with open('config.json', 'r', encoding="utf-8") as f:
			books = json.load(f)
		mangaLikeLibrary=[*books['mangaLike']]
		readComicOnlineToLibrary=[*books['readComicOnlineTo']]
		readComicsOnlineRuLibrary=[*books['readComicsOnlineRu']]
		comicExtraLibrary=[*books['comicExtra']]
		if not mangaLikeLibrary and not readComicOnlineToLibrary and not readComicsOnlineRuLibrary and not comicExtraLibrary :
			print("\nNo books found!\n")
			return
		print("\nList of books >")
		if mangaLikeLibrary:
			for i in mangaLikeLibrary:
				print (" > '"+i+"' download will start from Chapter-"+books['mangaLike'][i])
		if readComicOnlineToLibrary:
			for i in readComicOnlineToLibrary:
				print (" > '"+i+"' download will start from Chapter-"+books['readComicOnlineTo'][i])
		if readComicsOnlineRuLibrary:
			for i in readComicsOnlineRuLibrary:
				print (" > '"+i+"' download will start from Chapter-"+books['readComicsOnlineRu'][i])
		if comicExtraLibrary:
			for i in comicExtraLibrary:
				print (" > '"+i+"' download will start from Chapter-"+books['comicExtra'][i])

	except:
		raise
	comicMaker.mangaLike()
	comicMaker.readComicOnlineTo()
	comicMaker.readComicsOnlineRu()
	comicMaker.readComicsOnlineRu()
	comicMaker.comicExtra()
	print(" <<< All Downloads completed!\n")
	# return


if __name__ == '__main__':
	main()
