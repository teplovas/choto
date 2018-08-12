import requests
import bs4
from multiprocessing import Pool
import codecs

def parse_page(url):
    text = requests.get(url).text
    parser = bs4.BeautifulSoup(text, 'lxml')
    for img in parser.findAll('img', attrs={'class': 'thumbnail'}):
        url = 'https:' + img.get('src')
        download = requests.get(url)
        filename = url[url.rfind('/') + 1:]
        if (filename == "blank.gif"):
            continue
        with open("catalog/hat/wildberries/" + filename, "wb") as out:
            out.write(download.content)
            out.close()
        
    
p = Pool(10)
#url_list = ['https://www.wildberries.ru/catalog/zhenshchinam/odezhda/bluzki-i-rubashki/bluzki?page=' + str(n) for n in range(1, 101)]
url_list = ['https://www.wildberries.ru/catalog/aksessuary/golovnye-ubory/shapki?page=' + str(n) for n in range(1, 469)]

if __name__ == '__main__':    
    map_results = p.map(parse_page, url_list)