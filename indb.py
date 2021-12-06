#pip install influxdb before running this script
from influxdb import InfluxDBClient
from datetime import datetime
import urllib
import json
import pandas as pd
import numpy as np
import time,schedule,threading,datetime
import keras

#Set up the InfluxDB connection
client = InfluxDBClient(host='localhost', port=8086, database='telegraf')#testDB')
client.get_list_database() #확인하기
client.switch_database('telegraf')

def api():
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
    #api1['time']=api1['time'].str.replace(' ','T').str.replace(':00',':00:00Z')
    api1['time']=api1['time']+':00'
    api1['CO']=api1['CO'].astype(float)
    api1['PM10']=api1['PM10'].astype(float)
    api = api1.groupby(['time','region','geohash']).mean()
    api.reset_index(level=['time','region','geohash'], inplace = True)
    return api

def insertdb(api1,dbname):
    try:
        for y in range(len(api1)):
            json_payload = []
            data = {
                "measurement": dbname,
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
            print(data)
    except Exception as e:    # 모든 예외의 에러 메시지를 출력할 때는 Exception을 사용
        print('예외가 발생했습니다.', e)

def predict(df,guname):
    df2 = pd.read_csv('구변환(중복제거).csv')
    model = keras.models.load_model(guname+'.h5')

    co_past = np.array(df['CO'][-10:]).reshape(1,10,1)
    pm_past = np.array(df['PM10'][-10:]).reshape(1,10,1)

    dff = pd.DataFrame(columns=['time','region','CO','PM10'])

    current = datetime.datetime.now() # 1시간 후 
    
    for i in range(10):
        one_hour_later = current + datetime.timedelta(hours=i+1)
        future = model.predict([co_past,pm_past])
        dff = dff.append({'time':one_hour_later,'지역':df['region'].iloc[0],'CO' : future[0][0][0],'PM10' : future[1][0][0]}, ignore_index=True)
        co_past = np.delete(np.append(co_past,future[0]), 0).reshape(1,10,1)
        pm_past = np.delete(np.append(pm_past,future[1]), 0).reshape(1,10,1)
    dff=pd.merge(dff,df2,on='지역').drop(['region','측정소명'],axis=1)
    dff.rename(columns={'지역':'region'},inplace=True)
    dff = dff.drop_duplicates(['time'])
    return dff

def gudata(guname):
    re = client.query('select * from realtime')
    df = pd.DataFrame(re['realtime'])
    df = df[df['region']==guname]
    return df

def job():
    current = datetime.datetime.now() # 1시간 후 
    one_hour_later = current + datetime.timedelta(hours=1)
    one_hour_later = one_hour_later.strftime('%Y-%m-%d %H')
    client.query("delete from prophet where time > '"+one_hour_later+"'")
    
    api1 = api()#api로 실시간 데이터 구하고
    insertdb(api1,'realtime')#db에 저장

    guname = ['부산 강서구','부산 금정구','부산 기장군','부산 남구','부산 동구','부산 동래구','부산 부산진구','부산 북구','부산 사상구','부산 사하구','부산 서구','부산 수영구','부산 연제구','부산 영도구','부산 중구','부산 해운대구']
    for i in guname:
        df = gudata(i)
        dff = predict(df,i)
        # client.delete_series(database='telegraf',measurement='prophet',tags={'region':i})
        insertdb(dff,'prophet')

schedule.every(1).hours.do(job)#끝
while True:
    schedule.run_pending()