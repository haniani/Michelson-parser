# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib, re
from urllib import request

summary_links = []
summary_links_letter = []

page_first = urllib.request.urlopen('https://dic.academic.ru/contents.nsf/michelson_old/')
first_links = BeautifulSoup(page_first, 'html.parser')
for links in first_links.find_all(class_ = 'contents-wrap'):  #первый общий указатель
    for link in links.find_all('a'):
        summary_links.append('https:' + link.get('href'))

for i in summary_links: #второй общий указатель по букве
    page_second = urllib.request.urlopen(i)
    second_links = BeautifulSoup(page_second, 'html.parser')
    for links2 in second_links.find_all(class_ = 'terms-wrap'):
        for link2 in links2.find_all('a'):
            summary_links_letter.append(link2.get('href'))

with open("michelson_old.csv", 'w') as csv_file:
    for links3 in summary_links_letter:
        edit_links3 = links3.rsplit('/', 1)
        edited_links = edit_links3[0] + '/' #убираем кириллицу
        word_page = urllib.request.urlopen(edited_links)
        third_links = BeautifulSoup(word_page, 'html.parser') #словарная статья
        third_links = third_links.find("div", {"id": "article"})
        name = third_links.find('dt', {'class' : 'term'}) #слово
        paper = third_links.find('dd', {'class' : 'descript'}) #толкование
        word = name.getText()
        meaning = paper.getText()
        meaning = meaning.replace('\n','')
        write_mean_word = word + ' \t' + meaning + ' \n'
        writer = csv_file.write(str(write_mean_word))
