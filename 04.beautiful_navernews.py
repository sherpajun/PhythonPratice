
import urllib.request
from bs4 import BeautifulSoup

url='https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=102&oid=214&aid=0001152459'
res = urllib.request.urlopen(url)
soup =BeautifulSoup(res,'html.parser')


head = soup.select('ul.list_txt li a')
#print(len(head))
head_list=[]
for n in head:
    head_dic={}
    title = n['title'].strip()
    #print('제목:',title)
    head_dic['title']= title
    url = n['href']
    res = urllib.request.urlopen(url)
    soup =BeautifulSoup(res,'html.parser')
    content = soup.select_one('#articleBodyContents')
    zz=(content.text.replace('동영상 뉴스','').strip())
    #print(zz)
    head_dic['content']=zz
    head_list.append(head_dic)
    print(head_list)