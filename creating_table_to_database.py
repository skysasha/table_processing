#!/usr/bin/env python3
# -*- coding: utf8 -*-
import pandas as pd
import sqlalchemy as sa

import access_to_db

companies = pd.read_csv('tables/csv/companies.csv')
companies.to_sql(
    'companies_tv',
    con=access_to_db.engine,
    schema='blinov',
    if_exists='replace',        # понимаю, что очень плохо, но пока не могу судить, что "дешевле" -- заменять целиком или обновлять
    index=False,
    chunksize=10000,
    method=None,
    dtype={
        'companycode' : sa.String,
        'inn' : sa.String,
        'ogrn' : sa.String,
        'kpp' : sa.String,
        'name' : sa.String,
        'address' : sa.String,
        'hr-agency' : sa.String,
        'url' : sa.String,
        'site' : sa.String,
        'phone' : sa.String,
        'fax' : sa.String,
        'email' : sa.String,
    })

vacancies_r = pd.read_csv('tables/csv/vacancies.csv')
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
        'companycode' : sa.String,
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

vacancies_ext = pd.read_csv('tables/csv/vacancies_mrigo_okpdtr.csv')
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
        'companycode' : sa.String,
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