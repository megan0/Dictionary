import requests
from bs4 import BeautifulSoup
import re

def search_spider(url,max_lvl,file_name):
    niv = 1
    pattern = re.compile('((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*')
    fw = open('found_URL.txt','w')
    now = set()
    togo = set([url])
    temp = set()
    while niv <= max_lvl:
        if len(togo) != 0:
            for itemURL in togo:
                now.add(itemURL)
                source_code = requests.get(itemURL)
                plain_txt = source_code.text
                soup = BeautifulSoup(plain_txt,features="lxml")
                for link in soup.find_all('a'):
                    href = link.get('href')
                    if re.match(pattern,str(href)):
                        if href not in now:
                            temp.add(href)
            
            togo.clear()
            togo.update(temp)
            temp.clear()
            niv += 1
    for item in now:
        fw.write(str(item)+'\n')
                

if __name__ == "__main__":
    url = ' http://www.fshn.edu.al'
    search_spider(url,2,'found_URL.txt')




