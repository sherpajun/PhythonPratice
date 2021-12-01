import urllib
import json
import pandas as pd
import numpy as np
import time,schedule,threading
def reupload() :
    url='http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=zRFvHX1aXXCIImm6VM1r41s7qtk%2BZvLgs6in9M1REA4KFCxy9almfJetM4CgsUwUOATf7XkgGquTvNULLJtJ%2FA%3D%3D&returnType=json&numOfRows=100&pageNo=1&sidoName=%EB%B6%80%EC%82%B0&ver=1.0'
    result =json.load(urllib.request.urlopen(url))
    df2=pd.read('구변환(중복제거).csv')
    co = []
    pm10 = []
    date = []
    station = []
    for i in range(len(result['response']['body']['items'])) :
        co.append(result['response']['body']['items'][i]['coValue'])
        pm10.append(result['response']['body']['items'][i]['pm10Value'])
        date.append(result['response']['body']['items'][i]['dataTime'])
        station.append(result['response']['body']['items'][i]['stationName'])
    api=pd.DataFrame({'CO':co,'PM10':pm10,'time':date,'측정소명':station})
    api1=pd.merge(api,df2,how='outer',on='측정소명').drop('측정소명',axis=1)
    api1.rename(columns={'지역':'region'},inplace=True)
    api1 = api1.replace('-',np.nan)
    api1=api1.fillna(method='ffill')
    print(api1)
    api1.to_csv('ex.csv',index=False,encoding='utf-8-sig')

def 응애():
    print('정상실행')


schedule.every(1).hours.do(응애)#끝
while True:
    schedule.run_pending()
# if __name__ == '__main__':
#     threading.Timer(3,print('응애')).start()