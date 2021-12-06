#pip install influxdb before running this script
from influxdb import InfluxDBClient
from datetime import datetime
import urllib
import json
import pandas as pd
import numpy as np
import time,schedule,threading

#Set up the InfluxDB connection
client = InfluxDBClient(host='localhost', port=8086, database='tstest')#testDB')
client.get_list_database() #확인하기
client.switch_database('telegraf')

def test():
    #api 소환
    url='http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=zRFvHX1aXXCIImm6VM1r41s7qtk%2BZvLgs6in9M1REA4KFCxy9almfJetM4CgsUwUOATf7XkgGquTvNULLJtJ%2FA%3D%3D&returnType=json&numOfRows=100&pageNo=1&sidoName=%EB%B6%80%EC%82%B0&ver=1.0'
    result =json.load(urllib.request.urlopen(url))
    df2=pd.read_csv('구변환(중복제거).csv')
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
    api1['time']=api1['time'].str.replace(' ','T').str.replace(':00',':00:00Z')

    try:
        for y in range(len(api1)):
            json_payload = []
            data = {
                "measurement": "savetest",
                "tags":{
                    "region": api1["region"].iloc[y],
                    "geohash":api1["geohash"].iloc[y]
                },
                "time" : api1['time'].iloc[y], 
                "fields":{
                    "PM10":api1['PM10'].iloc[y],
                    "CO":api1['CO'].iloc[y]
                }
            }
            json_payload.append(data)
            client.write_points(json_payload)
            print(y,"번째 성공")
    except Exception as e:    # 모든 예외의 에러 메시지를 출력할 때는 Exception을 사용
        print('예외가 발생했습니다.', e)


schedule.every(1).hours.do(test)#끝
while True:
    schedule.run_pending()