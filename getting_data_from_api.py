#!/usr/bin/env python3
# -*- coding: utf8 -*-
from bs4 import BeautifulSoup
import html
import json
import numpy as np
import os
import pandas as pd
import re
import time
import urllib.request


def get_data_from_api(offset):
  with urllib.request.urlopen("http://opendata.trudvsem.ru/api/v1/vacancies/region/54?offset=" + str(offset) +"&limit=100") as url:
    data = json.loads(url.read().decode("utf-8"))
    status = int(data['status'])
    if status != 200:
      return None, status
  return data, status

def remove_tags(text):
  no_tags = re.sub(r'(<!--.*?-->|<[^>]*>)', '', text)
  return html.escape(no_tags)

def get_percent_of_null_in_columns(df):
    print(round((df.isnull().sum() * 100 / len(df)), 2).sort_values(ascending=False))


# start_time = time.time()

df_raw = pd.DataFrame()
offset = 0
while True:
  data, status = get_data_from_api(offset)
  if status != 200:
    break
  new_data = data['results']['vacancies']
  df_tmp = pd.io.json.json_normalize(new_data)
  df_raw = pd.concat([df_raw, df_tmp], sort=False, ignore_index=True)
  offset += 1
  
if not df_raw.empty:
  df_raw = df_raw.astype({
    'vacancy.region.region_code' : 'str',
    'vacancy.company.inn' : 'str',
    'vacancy.company.ogrn' : 'str',
    'vacancy.company.kpp' : 'str',
    'vacancy.addresses.address' : 'str',
    'vacancy.duty' : 'str',
    'vacancy.requirement.qualification' : 'str',
    })
  
  for index, row in df_raw.iterrows():
    df_raw.at[index, 'vacancy.region.region_code'] = re.split(r'[.]', df_raw.at[index, 'vacancy.region.region_code'])[0]
    df_raw.at[index, 'vacancy.company.inn'] = re.split(r'[.]', df_raw.at[index, 'vacancy.company.inn'])[0]
    df_raw.at[index, 'vacancy.company.ogrn'] = re.split(r'[.]', df_raw.at[index, 'vacancy.company.ogrn'])[0]
    df_raw.at[index, 'vacancy.company.kpp'] = re.split(r'[.]', df_raw.at[index, 'vacancy.company.kpp'])[0]
    df_raw.at[index, 'vacancy.addresses.address'] = re.sub("'location': |{|\[|lng': |'lat': |}|\]|\'", '', df_raw.at[index, 'vacancy.addresses.address'])
    df_raw.at[index, 'vacancy.duty'] = remove_tags(df_raw.at[index, 'vacancy.duty'])
    df_raw.at[index, 'vacancy.requirement.qualification'] = remove_tags(df_raw.at[index, 'vacancy.requirement.qualification'])
  df_raw = df_raw.replace({False : np.nan})
  df_raw = df_raw.replace({np.nan : None})
  df_raw.to_csv(os.path.join('tables', 'csv', 'raw_dataframe.csv'), index=None, header=True)
  # df_raw.to_excel('tables/excel/raw_dataframe.xlsx', index=None, header=True, engine='xlsxwriter')

# end_time = time.time()
# print(f"Time: {end_time - start_time}sec")