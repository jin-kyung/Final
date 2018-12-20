import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

A = input(print("please write the title you want to find in archive.org: "))

my_url = "https://archive.org/details/opensource_audio?sort=titleSorter&page="

page_number = 0
for all_page in range(133):
    all_page = my_url + str(page_number + 1)
    page_number += 1

    uClient = uReq(all_page)
    pages_html = uClient.read()
    uClient.close()

    soups = soup(pages_html, "html.parser")
    titles = soups.findAll('div', {"class":"ttl"})

    each_title = ' '
    for title in titles:
        each_title = each_title + title.text
    all_title = each_title.split("\n")

    for item in all_title:
        if A in item:
            print(item.lstrip())


