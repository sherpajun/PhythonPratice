
import requests
from bs4 import BeautifulSoup


url = 'https://finance.naver.com/marketindex/exchangeList.naver'
res= requests.get(url).text
soup =BeautifulSoup(res,'html.parser')

#soup.get_text
#print(soup.get_text)

#type(soup.td)
#print(soup.td)


#type(soup.td['a'])
#print(soup.td['a'])

#==========================================================#
name =[]
price=[]

result = soup.select('td.tit>a')
#print(result)
for a in result:
    ss=a.string.strip()
    #print(ss)
    name.append(ss)


result1 = soup.select('td.sale')
for td in result1:
    tt=td.string.strip()
    #print(tt)
    #print(float(tt.replace(',','')))
    tr = float(tt.replace(',',''))
    price.append(tr)

#print(name)
#print(price)

items = list(zip(name,price))#갯수가 동일한거 끼리 묶어준다.
print(items)


