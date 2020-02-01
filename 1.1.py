import requests
import re
num = 1
while True:
    r = requests.get('https://www.freebuf.com/articles/web/page/' + str(num))
    pattern = re.compile('<dt>.*?'+'href="(.*?)"'+'.*?</dt>',re.S)
    match = re.findall(pattern, r.text)    
    filename = open('url.txt', 'a')
    for value in match:
        filename.write(str(value))
    num = num + 1
    if int(r.status_code) > 200 :
        break
