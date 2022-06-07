import csv

import html5lib as html5lib
import requests

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re


thislist = ["y1", "y2", "y3"]

for y1 in thislist:
  y1 = ("https://www.indiegogo.com/individuals/8053268")
  html_page = urlopen(y1)
  soup = BeautifulSoup(html_page, "lxml")
  links = []
  for link in soup.findAll('a'):
    links.append(link.get('href'))

  for y2 in thislist:
    y2 = ("https://www.indiegogo.com/individuals/4590125")
    html_page = urlopen(y2)
    soup = BeautifulSoup(html_page, "lxml")
    ab = []
    for link in soup.findAll('a'):
      ab.append(link.get('href'))

    for y3 in thislist:
      y3 = ('https://www.indiegogo.com/individuals/23489031')
      html_page = urlopen(y3)
      soup = BeautifulSoup(html_page, "lxml")
      cd = []
      for link in soup.findAll('a'):
        cd.append(link.get('href'))




print(links)
print(ab)
print(cd)


print('')
print('')
print('')
print('')
print('')
print('')



from prettytable import PrettyTable



x = PrettyTable()

x.field_names = ["y", "Data"]

x.add_row(["y1", links])
x.add_row(["y2", ab])
x.add_row(["y3", cd])


print(x)



with open('x.csv', 'w', encoding='UTF8') as f:
  writer = csv.writer(f)

  # write the header
  writer.writerow(x)

  # write the data
  writer.writerow(links)









