from bs4 import BeautifulSoup
import requests
import json

monster = {
    "sorts": []
}

main_page = requests.get('https://www.d20pfsrd.com/bestiary/bestiary-alphabetical/')
soup = BeautifulSoup(main_page.content, 'lxml')

hrefList = soup.find('ul', {'class': 'ogn-childpages'})
# print(hrefList)

for link in hrefList.find_all('a'):
    page = requests.get(link.get('href'))
    soup_bis = BeautifulSoup(page.content, 'lxml')

    for td in soup_bis.find_all('td'):
        for h3 in td.find_all('h3'):
            h3.extract()
        for sup in td.find_all('sup'):
            sup.extract()
        for a in td.find_all('a', href=lambda href: href and "https://www.d20pfsrd.com/bestiary/" in href):
            print(a)
