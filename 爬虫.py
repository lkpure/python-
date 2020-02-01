import requests
import re
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'}
ym = requests.get('https://www.freebuf.com/articles/web/page/' + 'i',headers=headers)
for i in range(1,108):
    print(ym)
with open('yuanma.txt','w',encoding='utf-8') as f:
    f.write(ym.text)
    f.close
pattern = re.compile('<dt>.*?'+'href="(.*?)"'+'.*?</dt>',re.S)
match = re.findall(pattern,ym.text)
for i in match:
    print(i)
    ym2 = requests.get(i)
    with open('pageym.txt','a',encoding='utf-8') as f:
        f.write(ym2.text)
        f.close

