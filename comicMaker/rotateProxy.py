from lxml.html import fromstring
import requests,cfscrape,itertools,time
from multiprocessing.dummy import Pool
from sys import stdout
from bs4 import BeautifulSoup
from .checkInternet import checkInternet

class rotateProxy:
    
    def createProxyList(url):
        # proxyList=[]
        if not checkInternet():
            print("Could not connect, trying again in 5 seconds!")
            time.sleep(5)
            rotateProxy.createProxyList(url)
            return
        print("Finding Proxy Lists...Please wait...")
        linkThatHostsFreeProxies = 'https://free-proxy-list.net/anonymous-proxy.html'
        proxyList=[]
        proxies=[]
        # requests.packages.urllib3.disable_warnings()
        res = requests.get(linkThatHostsFreeProxies, headers={'User-Agent':'Mozilla/5.0'})
        soup = BeautifulSoup(res.text,"lxml")
        for items in soup.select("tbody tr"):
            proxy = ':'.join([item.text for item in items.select("td")[:2]])
            proxies.append(proxy)
        # print(proxies)
        # print(len(proxies))
        # return
        # with open("proxies.txt","wb") as f:
        #     pickle.dump(proxies, f)

        with Pool(len(proxies)) as pool:
            # proxyList.append(pool.starmap(rotateProxy.checkProxy, zip(proxies, itertools.repeat(url))))
            proxyList=(pool.starmap(rotateProxy.checkProxy, zip(proxies, itertools.repeat(url))))

        # print(proxyList)
        while (-1) in proxyList: proxyList.remove(-1)
        # proxyList.remove("-1")
        # print(proxyList)
        print("\n- "+str(len(proxyList))+" Working proxies found.")
        return proxyList

    def checkProxy(proxy,url):

        # with open(originalWorkingDirectory+os.sep+"proxies.txt","rb") as f:
        #     proxies=pickle.load(f)
        # proxies = createProxyList()
        # proxy_pool = cycle(proxies)
        # print(proxies)
        # url = 'https://httpbin.org/ip'
        # url="https://google.com"
        # print("Changing Proxy...")
        # for i in range(0,80):
        # Get a proxy from the pool
        # proxy = next(proxy_pool)
        # print("Request #%d"%i)
        try:
            # print(next(proxy_pool))
            # proxy = next(proxy_pool)
            # print("Request #%d"%i)
            # print(url)
            if not checkInternet():
                print("Could not connect, trying again in 3 seconds!")
                time.sleep(3)
                checkProxy(proxy,url)
                return
            scraper = cfscrape.create_scraper()
            # requests.packages.urllib3.disable_warnings()
            # response = scraper.get(url,proxies={"http": proxy, "https": proxy},headers={'User-Agent': 'Chrome'}, timeout=5)
            response = scraper.get(url,proxies={"https": proxy},headers={'User-Agent': 'Chrome'}, timeout=5)
            # response = requests.get(url,proxies={"http": proxy, "https": proxy})
            # print(response.json())
            
        except:
            # print(proxy+" Failed.")
            # proxies.remove(proxy)
            stdout.write("%s\r"%proxy)
            stdout.flush()
            # time.sleep(.1)
            # print("Bad Proxy", sep=' ', end='', flush=True)
            return(-1)
        else:
            # we will never run same proxy again
            # proxies.remove(proxy)
            stdout.write("XXX---Bad proxy---XXX\r")
            stdout.flush()
            # time.sleep(.1)
            # print(proxy, sep=' ', end='', flush=True)
            return(proxy)
            # with open(originalWorkingDirectory+os.sep+"proxies.txt","wb") as f:
            #     pickle.dump(proxies, f)
            # break
    #     print("Proxy found : "+proxy)
    #     return(proxy)

    # def removeProxy(proxy,originalWorkingDirectory):
    #     with open(originalWorkingDirectory+os.sep+"proxies.txt","rb") as f:
    #         proxies=pickle.load(f)
    #     proxies.remove(proxy)
    #     with open(originalWorkingDirectory+os.sep+"proxies.txt","wb") as f:
    #         pickle.dump(proxies, f)


    
# url="https://readcomiconline.to/Comic/"
# rotateProxy.createProxyList(url)