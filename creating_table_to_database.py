#!/usr/bin/env python3
# -*- coding: utf8 -*-
import numpy as np
import os
import pandas as pd
import re
import sqlalchemy as sa

import access_to_db


# vf_btr_lines_id_mrigo = pd.read_csv(os.path.join('tables', 'csv', 'id_mrigo_mrigo.csv'))
# vf_btr_lines_id_mrigo.to_sql(
#     'mrigo',
#     con=access_to_db.engine,
#     schema='blinov',
#     if_exists='replace',        # понимаю, что очень плохо, но пока не могу судить, что "дешевле" -- заменять целиком или обновлять
#     index=False,
#     chunksize=None,
#     method=None,
#     dtype={
#         'id_mrigo' : sa.String,
#         'mrigo' : sa.String,
#     })
# access_to_db.engine.execute('ALTER TABLE blinov.mrigo ADD PRIMARY KEY(id_mrigo)')

# okpdtr_id_name = pd.read_csv(os.path.join('tables', 'csv', 'id_okpdtr_okpdtr.csv'))
# okpdtr_id_name.to_sql(
#     'okpdtr',
#     con=access_to_db.engine,
#     schema='blinov',
#     if_exists='replace',
#     index=False,
#     chunksize=None,
#     method=None,
#     dtype={
#         'id' : sa.String,
#         'name' : sa.String,
#     })
# access_to_db.engine.execute('ALTER TABLE blinov.okpdtr ADD PRIMARY KEY(id)')

# companies = pd.read_csv(os.path.join('tables', 'csv', 'companies.csv'))
# companies = companies.astype({
#     'inn' : 'str',
#     'ogrn' : 'str',
#     'kpp' : 'str',
#     })
# for index, row in companies.iterrows():
#     companies.at[index, 'inn'] = re.split(r'[.]', companies.at[index, 'inn'])[0]
#     companies.at[index, 'ogrn'] = re.split(r'[.]', companies.at[index, 'ogrn'])[0]
#     companies.at[index, 'kpp'] = re.split(r'[.]', companies.at[index, 'kpp'])[0]
# companies = companies.replace({'nan' : np.nan})
# companies = companies.replace({np.nan : None})
# companies.to_sql(
#     'companies_tv',
#     con=access_to_db.engine,
#     schema='blinov',
#     if_exists='replace',
#     index=False,
#     chunksize=None,
#     method=None,
#     dtype={
#         'ogrn' : sa.String,
#         'inn' : sa.String,
#         'kpp' : sa.String,
#         'companycode' : sa.String,
#         'name' : sa.String,
#         'address' : sa.String,
#         'hr-agency' : sa.String,
#         'url' : sa.String,
#         'site' : sa.String,
#         'phone' : sa.String,
#         'fax' : sa.String,
#         'email' : sa.String,
#     })
# access_to_db.engine.execute('ALTER TABLE blinov.companies_tv ADD PRIMARY KEY(ogrn)')

vacancies_r = pd.read_csv(os.path.join('tables', 'csv', 'vacancies.csv'))
vacancies_r = vacancies_r.astype({
    'region_code' : 'str',
    'ogrn' : 'str',
    })
for index, row in vacancies_r.iterrows():
    vacancies_r.at[index, 'region_code'] = re.split(r'[.]', vacancies_r.at[index, 'region_code'])[0]
    vacancies_r.at[index, 'ogrn'] = re.split(r'[.]', vacancies_r.at[index, 'ogrn'])[0]
vacancies_r = vacancies_r.replace({'nan' : np.nan})
vacancies_r = vacancies_r.replace({np.nan : None})
vacancies_r.to_sql(
    'r_vacancies_tv',
    con=access_to_db.engine,
    schema='blinov',
    if_exists='replace',
    index=False,
    chunksize=None,
    method='multi',
    dtype={
        'id' : sa.String,
        'ogrn' : sa.String,
        'source' : sa.String,
        'region_code' : sa.String,
        'region_name' : sa.String,
        'address' : sa.String,
        'experience' : sa.String,
        'employment' : sa.String,
        'schedule' : sa.String,
        'job-name' : sa.String,
        'specialisation' : sa.String,
        'duty' : sa.String,
        'education' : sa.String,
        'qualification' : sa.String,
        'term_text' : sa.String,
        'social_protected' : sa.String,
        'salary_min' : sa.Float,
        'salary_max' : sa.Float,
        'salary' : sa.String,
        'currency' : sa.String,
        'vac_url' : sa.String,
        'creation-date' : sa.String,    # sa.DateTime,
        'modify-date' : sa.String,      # sa.DateTime,  
    })
access_to_db.engine.execute('ALTER TABLE blinov.r_vacancies_tv ADD PRIMARY KEY (id)')
access_to_db.engine.execute('ALTER TABLE blinov.r_vacancies_tv ADD CONSTRAINT r_vac_comp_f_key FOREIGN KEY (ogrn) REFERENCES blinov.companies_tv (ogrn)')

vacancies_ext = pd.read_csv(os.path.join('tables', 'csv', 'vacancies_mrigo_okpdtr.csv'))
vacancies_ext = vacancies_ext.astype({
    'region_code' : 'str',
    'ogrn' : 'str',
    'id_mrigo' : 'str',
    'id_okpdtr' : 'str',
    })
for index, row in vacancies_ext.iterrows():
    vacancies_ext.at[index, 'region_code'] = re.split(r'[.]', vacancies_ext.at[index, 'region_code'])[0]
    vacancies_ext.at[index, 'ogrn'] = re.split(r'[.]', vacancies_ext.at[index, 'ogrn'])[0]
    vacancies_ext.at[index, 'id_mrigo'] = re.split(r'[.]', vacancies_ext.at[index, 'id_mrigo'])[0]
    vacancies_ext.at[index, 'id_okpdtr'] = re.split(r'[.]', vacancies_ext.at[index, 'id_okpdtr'])[0]
vacancies_ext = vacancies_ext.replace({'nan' : np.nan})
vacancies_ext = vacancies_ext.replace({np.nan : None})
vacancies_ext.to_sql(
    'vacancies_tv',
    con=access_to_db.engine,
    schema='blinov',
    if_exists='replace',
    index=False,
    chunksize=None,
    method='multi',
    dtype={
        'id' : sa.String,
        'ogrn' : sa.String,
        'source' : sa.String,
        'region_code' : sa.String,
        'region_name' : sa.String,
        'address' : sa.String,
        'id_mrigo' : sa.String,
        'experience' : sa.String,
        'employment' : sa.String,
        'schedule' : sa.String,
        'job-name' : sa.String,
        'id_okpdtr' : sa.String,
        'specialisation' : sa.String,
        'duty' : sa.String,
        'education' : sa.String,
        'qualification' : sa.String,
        'term_text' : sa.String,
        'social_protected' : sa.String,
        'salary_min' : sa.Float,
        'salary_max' : sa.Float,
        'salary' : sa.String,
        'currency' : sa.String,
        'vac_url' : sa.String,
        'creation-date' : sa.String,    # sa.DateTime,
        'modify-date' : sa.String,      # sa.DateTime,  
    })
access_to_db.engine.execute('ALTER TABLE blinov.vacancies_tv ADD PRIMARY KEY(id)')
access_to_db.engine.execute('ALTER TABLE blinov.vacancies_tv ADD CONSTRAINT vac_comp_f_key FOREIGN KEY (ogrn) REFERENCES blinov.companies_tv (ogrn)')
access_to_db.engine.execute('ALTER TABLE blinov.vacancies_tv ADD CONSTRAINT vac_mrigo_f_key FOREIGN KEY (id_mrigo) REFERENCES blinov.mrigo (id_mrigo)')
access_to_db.engine.execute('ALTER TABLE blinov.vacancies_tv ADD CONSTRAINT vac_okpdtr_f_key FOREIGN KEY (id_okpdtr) REFERENCES blinov.okpdtr (id)')
