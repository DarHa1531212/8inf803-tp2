from bs4 import BeautifulSoup
import requests
import json

monsters = []

main_page = requests.get('https://www.d20pfsrd.com/bestiary/bestiary-alphabetical/')
soup = BeautifulSoup(main_page.content, 'lxml')

hrefList = soup.find('ul', {'class': 'ogn-childpages'})


def parse_monster_name(monster_name):
    stopWords = ["(3pp)", "(3pp)", "(3PP)", "[3pp]", "; 3pp", "3pp;", ", 3pp", "-3PP", "(3PP-FGG)", "(3pp:TOHC)", "(CR+2)"]
    if "Page Not Found" in monster_name:
        return []
    for word in stopWords:
        monster_name = monster_name.replace(word, "")
    monster_name = monster_name.replace('\u2019', "'")
    return monster_name.strip(" ")

def parse_monster_spell(monster_spell):
    return monster_spell.replace('\u2019', "'")


def find_spells(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'lxml')

    monster_name = parse_monster_name(soup.find('h1').get_text())
    if monster_name:
        print('--------------------------------')
        print(monster_name)
        print('--------------------------------')
    spells = soup.find_all('a', {'class': 'spell'})
    monster_spells = []

    for spell in spells:
        if monster_name:
            print(parse_monster_spell(spell.get_text()))
        monster_spells.append(parse_monster_spell(spell.get_text()))

    if monster_name:
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

with open('./results/result.json', 'w') as fout:
    fout.write('[' + ',\n'.join(json.dumps(monster) for monster in monsters) + ']\n')
