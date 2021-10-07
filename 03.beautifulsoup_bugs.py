import requests
from bs4 import BeautifulSoup

url='https://music.bugs.co.kr/chart'
res = requests.get(url).text
soup =BeautifulSoup(res,'html.parser')
# soup.get_text
# #print(soup.get_text)

# musiclist = []
# result = soup.select('tbody tr')
# for i in result(len(result)-2):
#     title = result[i].select_one('th p.title a').string.strip()
#     print(title)
#     artist =result[i].select_one('p.artist a').string.strip()
#     print(artist)
#     musiclist.append((title,artist))


# print(musiclist)
title_list=[]   
title = soup.select('th p.title a')
#print(len(title))
for a in title:
    #print(a.string)
    title_list.append(a.string)

artist_list=[]
artist =soup.select('td p.artist')
#print(len(artist))
for p in artist:
    a= p.text.strip()
    #print(a.replace('\n',''))
    artist_list.append(a.replace('\n',''))

resulte = list(zip(title_list,artist_list))
print(resulte)