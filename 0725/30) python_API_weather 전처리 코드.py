#!/usr/bin/env python
# coding: utf-8

#  https://wonhwa.tistory.com/entry/Python-%EA%B3%B5%EA%B3%B5%EB%8D%B0%EC%9D%B4%ED%84%B0-%ED%8F%AC%ED%84%B8%EC%9D%98-OPEN-API-%EC%82%AC%EC%9A%A9-%EB%B0%A9%EB%B2%952

# In[17]:


from urllib.parse import urlencode, unquote
import requests
import json

url = 'http://apis.data.go.kr/1360000/AsosHourlyInfoService/getWthrDataList'
queryString = "?" + urlencode(
{"ServiceKey": unquote('11s9FwTjB9PjiL7UlE7J5TLQ0%2F4hAosYOUj6Os71MYzgEP9sHS9bXqWIn%2BM1wmmdJDIDVKPGOlAp8nTADiw0jA%3D%3D'),
         'pageNo' : '1', 
         'numOfRows' : '10', 
         'dataType' : 'json', 
         'dataCd' : 'ASOS', 
         'dateCd' : 'HR', 
         'startDt' : '20220401', 
         'startHh' : '01', 
         'endDt' : '20220402', 
         'endHh' : '01', 
         'stnIds' : '108' }

)
queryURL = url + queryString
response = requests.get(queryURL,verify=False)
# url 불러오기
# response = requests.get(url)

#데이터 값 출력해보기
contents = response.text


# In[19]:


# 데이터 결과값 예쁘게 출력해주는 코드
pp = pprint.PrettyPrinter(indent=4)
print(pp.pprint(contents))


# In[20]:


#문자열을 json으로 변경
json_ob = json.loads(contents)
print(json_ob)
print(type(json_ob)) #json타입 확인


# In[22]:


# 필요한 내용만 꺼내기
body = json_ob['response']['body']['items']['item']
print(body)


# In[26]:


# pandas import
import pandas as pd
from pandas.io.json import json_normalize
# Dataframe으로 만들기
weather_df = json_normalize(body)
weather_df


# In[ ]:




