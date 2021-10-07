import requests
from bs4 import BeautifulSoup



url = 'http://www.cgv.co.kr/movies/'
res = requests.get(url).text
soup =BeautifulSoup(res,'html.parser')
soup.get_text
#print(soup1.get_text)

result = soup.select('strong.title')
for i in result:
    qq=i.string
    print(qq)