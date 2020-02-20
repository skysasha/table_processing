#!/usr/bin/env python
# -*- coding: utf8 -*-
from bs4 import BeautifulSoup
import pandas as pd


vacancies_ext = pd.read_csv('tables/csv/vacancies_mrigo_okpdtr.csv')

for s in vacancies_ext['duty']:
    print(s)
    print('##############################################')
    ss = BeautifulSoup(s, "lxml").get_text(strip=True)
    print(ss)
    print('##############################################')
