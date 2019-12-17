

<img align="left" width="80" src="docs/logo.png" alt="comicMaker project app icon">

# comicMaker  
[![Build Status](https://travis-ci.com/Gunjan933/comicMaker.svg?branch=master)](https://travis-ci.com/Gunjan933/comicMaker) [![Known Vulnerabilities](https://img.shields.io/badge/vulnerabilities%20-0-brightgreen.svg?style=flat)](https://snyk.io//test/github/Gunjan933/comicMaker?targetFile=requirements.txt) [![start with why](https://img.shields.io/badge/docs%20-passing-brightgreen.svg?style=flat)](https://github.com/Gunjan933/comicMaker/edit/master/README.md)  [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Gunjan933/comicMaker/graphs/contributors) [![python >=3.5](https://img.shields.io/badge/python->=3.5-blue.svg?style=flat)](#python-support) [![Gitter](https://badges.gitter.im/Gunjan933-comicMaker/community.svg)](https://gitter.im/Gunjan933-comicMaker/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

comicMaker is a command line tool which downloads Comics and Manga from various Manga and Comic sites and converts them into (lossless) pdf easily. This is for educational purpose only.

> Don't overuse this script. It puts loads on their servers.  
> Support the developers of those websites by disabling your adblock on their site.   
> Advertisments pay for the website servers.


<p align="center">
  <img src="docs/comiccharacters.jpg"> 
</p>

```
TL;DR :
step 1: Use "config.json" to enter desired comic book names, and from which chapter you want to download.  
step 2: Then enter following commands:  
        pip install -r requirements.txt
        python comicMaker.py
```


## Table of Content

* [Getting Started](#getting-started)
    * [Supported Sites](#supported-sites)
    * [Find Comic Book Name](#how-to-find-the-book-name)
    * [Configuring Downloads](#configuring-download-list)
* [Dependencies Installation](#dependencies-installation)
    * [Linux/Debian](#linuxdebian-)
    * [Windows](#windows-)
    * [Mac OS X](#mac-os-x-)
* [Python Support](#python-support)
* [Usage](#usage)
    * [Windows](#windows)
    * [Linux/Debian](#linuxdebian)
* [Features](#features)
    * [Save Location](#save-location)
    * [Working Principle](#how-the-program-works)
    * [Resource Management](#why-the-program-uses-this-much-resources)
* [Future Plans](#future-plans)
    * [Short Term](#short-term)
    * [Long Term](#long-term)
* [Known Bugs](#bugs)
* [Changelog](#changelog)
* [Opening An Issue/Requesting A Site](#opening-an-issuerequesting-a-site)
    * [Reporting Issues](#reporting-issues)
    * [Suggesting A Feature](#suggesting-a-feature)
* [License](#license)


<p align="center">
  <img src="docs/bookStore.jpg"> 
</p>

## Getting Started

### Supported Sites

URL can be any URL of the [supported websites](https://github.com/Gunjan933/comicMaker/blob/master/supported-sites.md).
  
| Supported Sites             	| Compatiability 	|
|-----------------------------	|----------------	|
| https://readcomiconline.to  	| 100%           	|
| https://readcomicsonline.ru 	| 100%           	|
| https://www.comicextra.com 	| 100%           	|
| https://mangalike.net       	| 90%            	|


### How to find the book name

Go to the required book website and see the URL. Find the book name, usually just after the "http://mangalike.net/manga/" or "https://readcomiconline.to/Comic/" part. If you want to download from start put `1` in the chapter part in the `config.json` file.

### Configuring download list

Find the file `config.json`. Inside there you can enter names of any books you want to download. And specify from which chapter you want to download. Here is an example:

```diff
+ Below is the content of "config.json" ->

{
    "mangaLike": {
        "chromosome-47" : "1",
        "haomen-tianjia-qianqi" : "35",
        "pulse" : "63"
        },
    "readComicOnlineTo": {
        "Civil-War-2006": "1",
        "Batman-The-Dark-Knight-Returns": "2",
        "X-Men-Origins-Jean-Grey": "1"
    },
    "readComicsOnlineRu": {
    
    },
    "comicExtra": {

    },
    "temporary library": {
        "tamen-de-gushi": "187",
        "otome-no-teikoku": "108.5"
    }
}  


+ This will download 6 books:
+ chromosome-47 , where downloads starts from chapter 1.
+ haomen-tianjia-qianqi , where download starts from chapter 35.
+ pulse , where download starts from chapter 63.
+ Civil-War-2006 , where download starts from chapter 1.
+ Batman-The-Dark-Knight-Returns , where download starts from chapter 2.
+ X-Men-Origins-Jean-Grey , where download starts from chapter 1.

- temporary library contains books that won't be downloaded by the program.


```
```diff
- Don't forget to put ',' between two books.
```


## Dependencies Installation
This script can run on multiple Operating Systems. You need `Node.js` in your system's path for this script to work (You need this on each and every Operating System, even on WINDOWS :/).   
Download the `Node.Js` from [Node.js official website](https://nodejs.org/en/). Doesn't matter which operating system you're on, this is a must. Follow the instructions mentioned below, according to your OS.

### Linux/Debian :
Since most (if not all) Linux/Debian OS come with python pre-installed, you don't have to install python manually. Make sure you're using python >= 3.5 though.

We need `pip` to install any external dependenc(ies). So, open any terminal and type in `pip list` and if it shows some data, then it is fine. But, if it shows error, like `pip not found` or something along this line, then you need to install `pip`. Just type this command in terminal :

```
sudo apt-get install python-pip
```

If you're on Fedora, CentOS/RHEL, openSUSE, Arch Linux, then you simply need to follow [`THIS TUTORIAL`](https://packaging.python.org/install_requirements_linux/) to install `pip`.

If this still doesn't work, then you'll manually need to install pip. Doing so is an easy one time job and you can follow   [`THIS TUTORIAL`](https://pip.pypa.io/en/stable/installing/) to do so.

* Download this [`requirements.text`](https://github.com/Gunjan933/comicMaker/blob/master/requirements.txt) file and put it in some directory/folder.
* Open terminal again and browse to the directory where you downloaded your requiremenets.txt file and run this command :
```
pip install -r requirements.txt
```
* It should install the required external libraries.



### Windows :
If you're on windows, then follow these steps :

* Install Python >= 3.5. Download the desired installer from [download Python](https://www.python.org/downloads/).
* [Add it in the system path](http://superuser.com/questions/143119/how-to-add-python-to-the-windows-path) (if not already added).
* Download this [`requirements.text`](https://github.com/Gunjan933/comicMaker/blob/master/requirements.txt) file and put it in some directory/folder.
* Open Command Prompt and browse to the directory where you downloaded your requiremenets.txt file and run this command :
```
pip install -r requirements.txt
```
* It should install the required external libraries.

Now, install Node.Js as well and make sure it's in your path.

Well, if everything came up good without any error(s), then you're good to go!

### Mac OS X :
Mac OS X users will have to fetch their version of `Python` and `Pip`.
* Python installation guide : [Install python on mac os X](http://docs.python-guide.org/en/latest/starting/install/osx/)
* Pip installation guide : [Installing pip on mac os X](http://stackoverflow.com/questions/17271319/installing-pip-on-mac-os-x)

After downloading and installing these, you need to add PIP & Python in your path. Follow [`THIS LITTLE GUIDE`](http://www.pyladies.com/blog/Get-Your-Mac-Ready-for-Python-Programming/) to install both, Python & pip successfully.


## Python Support

Supports python >= 3.5    

## Usage

Follow the instructions according to your OS :

### Windows
After you've saved this script in a directory/folder, you need to open `command prompt` and browse to that directory and then execute the script. Let's do it step by step :
* Open the folder where you've downloaded the files of this repository.
* Hold down the **`SHIFT`** key and while holding down the SHIFT key, **`RIGHT CLICK`** and select `Open Command Prompt Here` from the options that show up.
* Now, in the command prompt, type this :

```
python comicMaker.py
```

<p align="center">
  <img src="docs/terminal.gif"  width="500"> 
</p>


### Linux/Debian
After you've saved this script in a directory/folder, you need to open `command prompt` and browse to that directory and then execute the script. Let's do it step by step :
* Open a terminal, `Ctrl + Alt + T` is the shortcut to do so (if you didn't know).
* Now, change the current working directory of the terminal to the one where you've downloaded this repository.
* Now, in the Terminal, type this :
```
python comicMaker.py
```

## Features

- This will download all the images from a chapter in a folder.
- Progressbar added for getting realtime downloading status.
- This will also create pdf for each chapters.
- This will merge all chapter pdfs into a single one as a full book after completing downloading each book.
- Added proxy support from [Free Proxy List](https://free-proxy-list.net/anonymous-proxy.html) for anonymous downloading and to avoid getting banned.
- Used multithreading for parallel downloading.

### Save Location

Comics will be saved on the same directory you clone this repository. Here is how: 
```diff
-     --SomeDirectory (Where you cloned the repository)
        |--comicMaker
-       |  |--comicMaker
        |  |  |--__init__.py
        |  |  |--(and some necessary modules the program needs)
        |  |--requirements.txt
        |  |--.gitignore
        |  |--_config.yml
        |  |--comicMaker.py
        |  |--config.json
        |  |--readme.md
-       |--comicDownloads
        |  |--chromosome-47
        |  |--haomen-tianjia-qianqi
        |  |--pulse 

```

 
### How the program works  

- The comic pages are not hosted in "https://www.mangalike.net/". So the program goes in each chapter, looks into all of the image sources, gets all the links, saves them in location.
- To convert to pdfs, any image should not contain any alpha channel. So every image is converted in RGB after downloading.
- In system the sorted page numbers looks like `(if page range is-(0-111)) then [0,1,10,11,100,101,110,111,2,20,21,3..,99]`. We can't create pdf with this order, so we have to sort them by standard `[0,1,2,3,..,110,111]`, and then make pdf.
- After completing every book, all the pdfs under each chapters, are merged into a single one, so that merged pdf will contain the whole book.


### Why the program uses this much resources
- This Download iterates to over 2000 pages average for each book. (Approximately each chapter contains 15 pages, and there are over 150 chapters each book). So it will take ages to download every file at each iteration.
- Here comes **multithreading**. With this, every files are downloaded simultaneously -
  - **Minimum :** It you have a `4 core CPU`, you can start downloading `8 files at once`.  ( In cases where the number of files is less than `2 x cpu-core-count` )
  - **Maximum :** It can download maximum of `90 files at once`.

## Future plans

### Short term 

- Download only selected chapters from each book (`config.json` file should take that data)
- Right now it can only download books from [Manga Like](http://mangalike.net/) which are divided only in chapters, not volumes. It should also be able to download if the book contains "Volumes".

### Long term

- Add more websites to download from.
- Add command line arguments for ease of use.
- Add documentation of how each code snippet works.

## Bugs

- (Non-Problamatic) The free proxies from [FreeProxyList](https://free-proxy-list.net/anonymous-proxy.html) are anonymous and elite but limited and slow.

## Changelog

- [Added]  New website [Comic Extra](https://www.comicextra.com/)
- [Added]  New website [Read Comics Online](https://readcomicsonline.ru/)
- [Added]  Proxy support from [Free Proxy List](https://free-proxy-list.net/anonymous-proxy.html) for mass downloading without getting banned.
- [Added]  New website [Read Comic Online](https://readcomiconline.to/)
- [Added]  Optimize downloading process for taking less resources.
- [Fixed]  (Non-Problamatic) The pdf merging continues, even if the book is completely downloaded.
- [Fixed]  (Problamatic) Image to pdf fails if images are not downloaded completely.
- [Fixed]  (Problamatic) Can't convert RGBA images in pdf.
- [Fixed]  (Problamatic) If connection fails, the total downloading fails.
- [Fixed]  (Problamatic) Pdfs are merged out of order.
- [Added]  New website [Manga Like](https://mangalike.net/)

## Opening An Issue/Requesting A Site

If your're planning to open an issue for the script or ask for a new feature or anything that requires opening an Issue, then please do keep these things in mind.

### Reporting Issues

If you're going to report an issue, please follow this syntax :  
**Command You Gave** : What was the command that you used to invoke the issue?  
**Expected Behaviour** : After giving the above command, what did you expect shoud've happened?  
**Actual Behaviour** : What actually happened?  
**Error Log** : Error Log is mandatory.  

 
### Suggesting A Feature
  
If you're here to make suggestions, please follow the basic syntax to post a request :  
**Subject** : Something that briefly tells us about the feature.  
**Long Explanation** : Describe in details what you want and how you want.  

## License
[MIT](https://github.com/Gunjan933/comicMaker/blob/master/LICENSE)
