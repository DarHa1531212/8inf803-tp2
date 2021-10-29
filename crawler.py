from bs4 import BeautifulSoup
import requests
import json

monster = {
    "sorts": []
}

main_page = requests.get('https://www.d20pfsrd.com/bestiary/bestiary-alphabetical/')
soup = BeautifulSoup(main_page.content, 'lxml')

hrefList = soup.find('ul', {'class': 'ogn-childpages'})
#print(hrefList)

for link in hrefList.find_all('a'):
    page = requests.get(link.get('href'))
    soup_bis = BeautifulSoup(page.content, 'lxml')

    for link2 in hrefList.find_all():









