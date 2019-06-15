import requests
from bs4 import BeautifulSoup
import re

def search_spider(url,max_lvl,file_name):
    niv = 1
    pattern = re.compile('((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*')
    fw = open('found_URL.txt','w')
    URL_visited = set()
    URL_to_visit = set([url])
    URL_temp = set()
    while niv <= max_lvl:
        print(len(URL_to_visit))
        if len(URL_to_visit) != 0:
            for itemURL in URL_to_visit:
                URL_visited.add(itemURL)
                source_code = requests.get(itemURL)
                plain_txt = source_code.text
                soup = BeautifulSoup(plain_txt,features="lxml")
                for link in soup.find_all('a'):
                    href = link.get('href')
                    if re.match(pattern,str(href)):
                        if href not in URL_visited:
                            URL_temp.add(href)
            
            #print(len(URL_temp))
            URL_to_visit.clear()
            URL_to_visit.update(URL_temp)
            URL_temp.clear()
            #print(len(URL_temp))
            #print(URL_to_visit)
            niv += 1
    for item in URL_visited:
        fw.write(str(item)+'\n')
                

if __name__ == "__main__":
    url = ' http://www.fshn.edu.al'
    search_spider(url,2,'found_URL.txt')




