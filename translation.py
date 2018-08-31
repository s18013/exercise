#! /usr/bin/python3
from itertools import chain
import requests, webbrowser, bs4, sys


#英文を引数として所得し単語ごとに分割
element = sys.argv[1:]


#記号、重複の削除
#element_unique = sorted(set(element), key=element.index)
element = [s.replace(',', ' ') for s in element]
element = [s.replace('!', '') for s in element]
element = [s.replace('.', ' ') for s in element]

#element = [s.replace('\'', '') for s in element] #検索されな不具合が出るため保留
#element = [s.replace('?', '') for s in element] #検索されな不具合が出るため保留

element = [s.split() for s in element]
element = list(chain.from_iterable(element))
element = sorted(set(element), key=element.index)

#print(len(element[0]))
#print(len(element))

#element_unique = sorted(set(element), key=element.index)
#print(element_unique)

#接続詞や意味の簡単な単語の削除
element_number = len(element)
pick_up = []
for i in range(element_number):
    if len(element[i]) > 3:
        pick_up.append(element[i])

print(pick_up)
#pick_up = [s.replace(',', ' ') for s in pick_up]
#pick_up = [s.split() for s in pick_up]

#list(chain.from_iterable(pick_up))



# elementをwebで検索しブラウザで表示
for i in range(len(pick_up)):
    webbrowser.open('http://www.google.co.jp/search?q={}  日本語訳'.format(pick_up[i]))

#res = requests.get('http://www.google.co.jp/search?q=' + ' '.join(sys.argv[1:]))
#res.raise_for_status()


# 結果と単語を並べる
#print('downloading{}...'.format('http://www.google.co.jp/search?q={} 日本語訳'.format(pick_up)))
