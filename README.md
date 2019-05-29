# comicMaker  
###  -- Download any comic from https://www.mangalike.net/ --  
  
  

### TL;DR:
Set comic book names in `config.json` file. And run `comicMaker.py`.

## Performance:

**4 chapters/minute on 4 core CPU and 1MBPS internet connection.**

## Usage:

### Step 1 :  
Find the file `config.json`. Inside there you can enter names of any books you want to download. And specify from which chapter you want to download. Here is an example:

```diff
{
    "chromosome-47" : "1",
    "haomen-tianjia-qianqi" : "35",
    "pulse" : "63"
}  


- This will download 3 books:
+ chromosome-47 , where downloads starts from chapter 1.
+ haomen-tianjia-qianqi , where download starts from chapter 35.
+ pulse , where download starts from chapter 63.
```
```diff
- Don't forget to put ',' between two books.
```

#### How to find the book name:  

Go to the required book website and see the URL. Find the book name, usually just after the http://mangalike.net/manga/ part. If you want to download from start put `1` in the chapter part in the `config.json` file.

### Step 2 : 

After entering the valid books in the file `config.json`, press `SHIF+RIGHT-MOUSE-BUTTON` to open up termnial.  
First run the following command:

```
pip install -r requirements.txt
```

This will download all required modules the program requires.  

### Step 3 :

Then enter the following command:

```
python comicMaker.py
```

### Trick :

The program will automatically detect the books you want to download. It will check for your CPU core count, and run accordingly, with **multiprocessing** for burst speed.

### Save Location :

Comics will be saved on the same directory you clone this repository. Here is how: 
```
 --SomeDirectory (Where you cloned the repository)
  |--comicMaker
  |  |--comicMaker
  |  |  |--__init__.py
  |  |  |--(and some necessary modules the program needs)
  |  |--requirements.txt
  |  |--.gitignore
  |  |--_config.yml
  |  |--comicMaker.py
  |  |--config.json
  |  |--readme.md
  |--comicDownloads
  |  |--chromosome-47
  |  |--haomen-tianjia-qianqi
  |  |--pulse 

```

## Features:

- This will download all the images from a chapter in a folder.
- Progressbar added for getting realtime downloading status.
- This will also create pdf for each chapters.
- This will merge all chapter pdfs into a single one as a full book after completing downloading each book.

## Insights:
 
 ### How the program works ?  
- The comic pages are not hosted in "https://www.mangalike.net/". So the program goes in each chapter, looks into all of the image sources, gets all the links, saves them in location.
- To convert to pdfs, any image should not contain any alpha channel. So every image is converted in RGB after downloading.
- In system the sorted page numbers looks like `(if page range is-(0-111)) then [0,1,10,11,100,101,110,111,2,20,21,3..,99]`. We can't create pdf with this order, so we have to sort them by standard `[0,1,2,3,..,110,111]`, and then make pdf.
- After completing every book, all the pdfs under each chapters, are merged into a single one, so that merged pdf will contain the whole book.

### Why the program uses this much resources ?  
- This Download iterates to over 2000 pages average for each book. (Approximately each chapter contains 15 pages, and there are over 150 chapters each book). So it will take ages to download every file at each iteration.
- Here comes **multiprocessing**. With this, number of processes at each iterations is increased to 2 times the core count of your computer's CPU.
- It you have a `4 core CPU`, you can start downloading `8 files at once`.

## Future plans:

### Short term :  

- Download only selected chapters from each book (`config.json` file should take that data)
- Optimize downloading process for taking less resources.
- Right now it can only download books which are divided only in chapters, not volumes. It should also be able to download if the book contains "Volumes".

### Long term :  

- Add more websites to download from.
- Add command line arguments for ease of use.
- Add documentation of how each code snippet works.

## Bugs:

You tell!
