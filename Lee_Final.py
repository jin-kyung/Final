import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://archive.org/details/opensource_audio?sort=titleSorter&page="

A = input(print("please type music title or keyword you want to search: "))

page_number = 0
for all_page in range(133):
    all_page = my_url + str(page_number + 1)
    page_number += 1

    uClient = uReq(all_page)
    pages_html = uClient.read()
    uClient.close()

    soups = soup(pages_html, "html.parser")

    containers = soups.findAll('div', {"class": "C234"})

    for container in containers:
        creators = container.findAll('span', {"class": "byv"})
        titles = container.findAll('div', {"class": "ttl"})

        each_title = ' '
        for title in titles:
            each_title = each_title + title.text

        each_creator = ' '
        for creator in creators:
            each_creator = each_creator + creator.text

        lists = "title: " + each_title.lstrip() + ",   " + "creator: " + each_creator.lstrip()

        if A in lists:
            print(lists)


