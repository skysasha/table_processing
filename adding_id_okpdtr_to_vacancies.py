#!/usr/bin/env python3
# -*- coding: utf8 -*-
from bs4 import BeautifulSoup
import jellyfish
import numpy as np
import pandas as pd
import re
from string import digits

import preparing_text
import okpdtr_splits


vacancies = pd.read_csv('tables/csv/vacancies_mrigo.csv')
okpdtr_id_name = pd.read_csv('tables/csv/id_okpdtr_okpdtr.csv')

id_okpdtr_lst = okpdtr_id_name['id'].tolist()
okpdtr_lst = okpdtr_id_name['name'].tolist()
okpdtr_lst_raw = okpdtr_lst.copy()
job_lst = vacancies['job-name'].tolist()

for i in range(len(okpdtr_lst)):
  okpdtr_lst[i] = re.sub(r'\(|\)|[,]','', re.sub('-', ' ', str(okpdtr_lst[i])).lower())

for i in range(len(job_lst)):
  job_lst[i] = re.sub(r'[^\w\s]', '', re.sub('-', ' ', str(job_lst[i])).lower())  # удаляем служебные символы, переводим в ниж. регистр
  remove_digits = str.maketrans('', '', digits)
  job_lst[i] = job_lst[i].translate(remove_digits)                                # удаляем цифры
  job_lst[i] = re.split(r'{}'.format('|'.join(okpdtr_splits.dictionary)), job_lst[i])[0]
    
indexes = []
for i in range(len(job_lst)):
  sub_lst = []
  for j in range(len(okpdtr_lst)):
    sub_lst.append(jellyfish.jaro_distance(okpdtr_lst[j], job_lst[i]))
  max_indexes = preparing_text.find_locate_max(sub_lst)
  if max_indexes[0] < 0.84:
    indexes.append(len(okpdtr_lst))
  else:
    indexes.append(max_indexes[1][0])
id_okpdtr_lst.append(None)
okpdtr_lst.append(None)

vacancies.insert(11, 'id_okpdtr', [id_okpdtr_lst[indexes[i]] for i in range(len(job_lst))], True)
vacancies.to_csv('tables/csv/vacancies_mrigo_okpdtr.csv', index=None, header=True)
# vacancies.to_excel('tables/excel/vacancies_with_id_okpdtr.xlsx', index=None, header=True, engine='xlsxwriter')

vacancies_job_id_okpdtr = vacancies[['job-name', 'id_okpdtr']]
okpdtr_lst_raw.append(None)
vacancies_job_id_okpdtr.insert(2, 'okpdtr', [okpdtr_lst_raw[indexes[i]] for i in range(len(job_lst))], True)
print(vacancies_job_id_okpdtr.isna().sum())
vacancies_job_id_okpdtr.to_csv('tables/other_csv/vacancies_jobname_okpdtr_id_okpdtr.csv', index=None, header=True)