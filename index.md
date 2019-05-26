# comicMaker
## Download any comic from https://www.mangalike.net

**TL;DR**
Set download links in "links.txt" file. And run "comicmaker.py".

## Usage:

Find the file "link.txt" .Inside there you can enter links of any books you want to download. "#" is used for commenting out the URLs you don't want to download, or already downloaded. Here is an example:

> https://www.mangalike.net/manga/chromosome-47/chapter-9

As long as the book name is inside the link, you are safe to proceed.

> https://www.mangalike.net/manga/chromosome-47

This is also a valid link!

> #https://www.mangalike.net/manga/chromosome-47

This link will be ignored while downloading.

After entering the valid links in the file "links.txt",
Open terminal and run the following command:

> python comicMaker.py

The program will automatically detect the books you want to download. It will check for your CPU core count, and run accordingly, with **multiprocessing** for burst speed.

## Features:

- This will download all the images from a chapter in a folder.
- Progressbar added for getting realtime downloading status.
- This will also create pdf for each chapters.
- This will merge all chapter pdfs into a single one as a full book after completing downloading each book.

## Insights:
 
- The comic pages are not hosted in "https://www.mangalike.net/". So the program goes in each chapter, looks into all of the image sources, gets all the links, saves them in location.
- To convert to pdfs, any image should not contain any alpha channel. So every image is converted in RGB after downloading.
- In system the sorted page numbers looks like (if page range is-(0-111))[0,1,10,11,100,101,110,111,2,20,21,3..,99]. We can't create pdf with this order, so we have to sort them by standard[0,1,2,3,..,110,111], and then make pdf.
- After completing every book, all the pdfs under each chapters, are merged into a single one, so that merged pdf will contain the whole book.
- This Download iterates to over 2000 pages average for each book. (Approximately each chapter contains 15 pages, and there are over 150 chapters each book). So it will take ages to download every file at each iteration.
- Here comes **multiprocessing**. With this, number of processes at each iterations is increased to 2 times the core count of your computer's CPU.
- It you have a 4 core CPU, you can start downloading 8 files at once.

## To-Do:

Create a module that starts downloading from desired chapters like (download from chapter 21). Right now it downloads from first to last.

## Bugs:

If internet gets disconnected while saving image, the images are saved partially(and the program doesn't download that image again, as it still can't detect if the image is saved partially or not), and this raises an error while making the pdfs.