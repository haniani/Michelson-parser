# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib
from urllib import request
from urllib.parse import quote

html_doc = urllib.request.urlopen('https://dic.academic.ru/contents.nsf/michelson_new/')
soup_links = BeautifulSoup(html_doc, 'html.parser')

summary_links = []
summary_links_letter = []

'''
for links in soup_links.find_all(class_ = 'contents-wrap'):  #первый общий указатель
    for link in links.find_all('a'):
        summary_links.append('https:' + link.get('href'))

for i in summary_links:
    site = urllib.request.urlopen(i)
    bs_links = BeautifulSoup(site, 'html.parser')
    for links2 in soup_links.find_all(class_ = 'terms-wrap'):  #второй общий указатель по букве
        for link2 in links2.find_all('a'):
            summary_links_letter.append('https:' + link2.get('href'))

for l in summary_links_letter:
    site2 = urllib.request.urlopen(l)
    bs_links2 = BeautifulSoup(site2, 'html.parser')
    bs_links2 = bs_links2.find("div", {"id": "article"})
    print(bs_links2)
'''
page_id = 1
with open("michelson_new.csv", 'w') as csv_file:
    while page_id != 10:
        site_2 = 'https://dic.academic.ru/dic.nsf/michelson_new/' + str(page_id) +'/'
        page_id += 1
        site2 = urllib.request.urlopen(site_2)
        bs_links2 = BeautifulSoup(site2, 'html.parser')
        bs_links3 = bs_links2.find("div", {"id": "article"})
        name = bs_links3.find('dt', {'class' : 'term'}) #слово
        bs_links4 = bs_links3.find('dd', {'class' : 'descript'}) #толкование
        word = name.getText()
        meaning = bs_links4.getText()
        meaning = meaning.replace('\n','')
        write_mean_word = word + ' \t' + meaning + ' \n'
        print(write_mean_word)
        writer = csv_file.write(str(write_mean_word))

