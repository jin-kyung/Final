import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


my_url = "https://archive.org/details/opensource_audio?sort=titleSorter&page=1"

uClient = uReq(my_url)
pages_html = uClient.read()
uClient.close()

soups = soup(pages_html, "html.parser")

containers = soups.findAll('div', {"class": "C234"})

A = input(print("please: "))
for container in containers:
    creators = container.findAll('span', {"class": "byv"})
    titles = container.findAll('div', {"class": "ttl"})

    each_creator = ' '
    for creator in creators:
        each_creator = each_creator + creator.text

    each_title = ' '
    for title in titles:
        each_title = each_title + title.text

        lists = "title: " + each_title.lstrip() + ",   " + "creator: " + each_creator.lstrip()

        if A in lists:
            print(lists)



