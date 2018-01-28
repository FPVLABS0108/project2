import requests
from bs4 import BeautifulSoup

def web_crawler(max_pages):
    page=1
    while page<=max_pages:
        page_url="https://github.com/python?page=" +str(page)
        get_source_code=requests.get(page_url)
        plaintext= get_source_code.text
        soup=BeautifulSoup(plaintext)
        for link in soup.findAll('a',{'itemprop':'name codeRepository'}):
            get_href= "https://github.com" +link.get('href')
            print(get_href)
        page+=1




web_crawler(1)




