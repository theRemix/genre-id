#! /usr/bin/env python3

"""
usage: genre-id.py [-h] [-v] [-vv] query [query ...]

ID Genre from Beatport

positional arguments:
  query       Song Artist + Title query

optional arguments:
  -h, --help  show this help message and exit
  -v          Print first song name and genre
  -vv         Print all song names, artists, remixers, and genres

examples:

./genre-id.py Major7 Closer

output:

Psy-Trance



./genre-id.py -v Major7 Closer

output:

Name         Genre
-----------  ----------
Closer       Psy-Trance
Bamboozled   Psy-Trance
Inequality   Psy-Trance
Moonlight    Psy-Trance
Psychotic    Psy-Trance
Glide        Psy-Trance
Look Around  Psy-Trance



./genre-id.py -vv Major7 Closer

output:

Name         Artist                 Remixers    Genre
-----------  ---------------------  ----------  ----------
Closer       Major7                             Psy-Trance
Bamboozled   Major7                             Psy-Trance
Inequality   Major7                             Psy-Trance
Moonlight    Major7, Rexalted                   Psy-Trance
Psychotic    Major7, D-Addiction                Psy-Trance
Glide        Major7, Invader Space              Psy-Trance
Look Around  Major7, Rexalted                   Psy-Trance

"""

import argparse
from urllib.parse import urlencode
from requests import get
from bs4 import BeautifulSoup
from tabulate import tabulate

parser = argparse.ArgumentParser(description='ID Genre from Beatport')
parser.add_argument('query', nargs='+',
                    help='Song Artist + Title query')
parser.add_argument('-v', action='store_true', help='Print first song name and genre')
parser.add_argument('-vv', action='store_true', help='Print all song names, artists, remixers, and genres')
args = parser.parse_args()

url = 'https://www.beatport.com/search'
params = urlencode({
    'q': ' '.join(args.query),
    '_pjax': '%23pjax-inner-wrapper' # request partial page
})
dataParamName='data-ec-name'
dataParamArtist='data-ec-d1'
dataParamRemixers='data-ec-d2'
dataParamGenre='data-ec-d3'

def liToTableV(li):
    return [li[dataParamName], li[dataParamGenre]]

def liToTableVV(li):
    return [li[dataParamName], li[dataParamArtist], li.get(dataParamRemixers), li[dataParamGenre]]

def display(lis):
    if args.vv:
        print(tabulate(map(liToTableVV, lis), headers=['Name', 'Artist', 'Remixers','Genre']))
    elif args.v:
        print(tabulate(map(liToTableV, lis), headers=['Name', 'Genre']))

    else:
        print(lis[0][dataParamGenre])


r = get(f'{url}?{params}')

soup = BeautifulSoup(r.text, 'html.parser')

releases = soup \
    .find('div', class_='bucket releases') \
    .find_all('li', class_='bucket-item')

display(releases)
