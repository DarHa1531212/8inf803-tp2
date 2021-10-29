from bs4 import BeautifulSoup
import requests
import json

monsters = []

main_page = requests.get('https://www.d20pfsrd.com/bestiary/bestiary-alphabetical/')
soup = BeautifulSoup(main_page.content, 'lxml')

hrefList = soup.find('ul', {'class': 'ogn-childpages'})


def find_spells(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'lxml')

    monster_name = soup.find('h1').get_text()
    print(monster_name)

    spells = soup.find_all('a', {'class': 'spell'})
    monster_spells = []

    for spell in spells:
        print(spell.get_text())
        monster_spells.append(spell.get_text())

    monsters.append({"name": monster_name, "spells": monster_spells})


def find_monsters_and_spells(link):
    page = requests.get(link.get('href'))
    soup_bis = BeautifulSoup(page.content, 'lxml')
    for td in soup_bis.find_all('td'):
        for h3 in td.find_all('h3'):
            h3.extract()
        for sup in td.find_all('sup'):
            sup.extract()
        for a in td.find_all('a', href=lambda href: href and "https://www.d20pfsrd.com/bestiary/" in href):
            find_spells(a.get('href'))


for link in hrefList.find_all('a'):
    find_monsters_and_spells(link)

with open('./results/result.json', 'w') as json_file:
    json.dumps(monsters, json_file)
