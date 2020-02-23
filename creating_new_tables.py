#!/usr/bin/env python3
# -*- coding: utf8 -*-
import os
import pandas as pd
import re


df = pd.read_csv(os.path.join('tables', 'csv', 'raw_dataframe.csv'))
df = df[pd.notnull(df['vacancy.company.ogrn'])]

if not df.empty:
  # for index, row in df.iterrows():
  #   df.at[index, 'vacancy.addresses.address'] = re.sub("'location': |{|\[|lng': |'lat': |}|\]|\'", '', df.at[index, 'vacancy.addresses.address'])
  # 'vacancy.company.code_industry_branch' и 'vacancy.category.industry' не рассматриваем, так как в записях практически нет информации;
  # в случае 'vacancy.company.code_industry_branch' - нет ни одной записи с не NULL-значением
  companies = df[
    [ 'vacancy.company.companycode', 'vacancy.company.inn', 'vacancy.company.ogrn', 'vacancy.company.kpp',
    'vacancy.company.name',
    'vacancy.addresses.address',
    'vacancy.company.hr-agency',
    'vacancy.company.url', 'vacancy.company.site',
    'vacancy.company.phone', 'vacancy.company.fax', 'vacancy.company.email',
    'vacancy.company.code_industry_branch',
    ]]
  companies = companies.drop_duplicates(subset="vacancy.company.inn", keep='first')
  companies = companies.reset_index(drop=True)
  companies = companies.rename(columns={
    'vacancy.company.ogrn' : 'ogrn',
    'vacancy.company.inn' : 'inn',
    'vacancy.company.kpp' : 'kpp',
    'vacancy.company.companycode' : 'companycode',
    'vacancy.company.name' : 'name',
    'vacancy.addresses.address' : 'address',
    'vacancy.company.hr-agency' : 'hr-agency',
    'vacancy.company.url' : 'url',
    'vacancy.company.site' : 'site',
    'vacancy.company.phone' : 'phone',
    'vacancy.company.fax' : 'fax',
    'vacancy.company.email' : 'email',
    'vacancy.company.code_industry_branch' : 'code_industry_branch',
    })
  companies.to_csv(os.path.join('tables', 'csv', 'companies.csv'), index=None, header=True)
  # companies.to_excel('tables/excel/companies.xlsx', index=None, header=True, engine='xlsxwriter')
  
  vacancies = df[
    ['vacancy.id', 'vacancy.company.ogrn',
    'vacancy.source',
    'vacancy.region.region_code', 'vacancy.region.name', 'vacancy.addresses.address',
    'vacancy.requirement.experience',
    'vacancy.employment', 'vacancy.schedule',
    'vacancy.job-name', 'vacancy.category.specialisation', 'vacancy.duty',
    'vacancy.requirement.education', 'vacancy.requirement.qualification',
    'vacancy.term.text', 'vacancy.social_protected',
    'vacancy.salary_min', 'vacancy.salary_max', 'vacancy.salary', 'vacancy.currency',
    'vacancy.vac_url',
    'vacancy.category.industry',
    'vacancy.creation-date', 'vacancy.modify-date',
    ]]

  vacancies = vacancies.rename(columns={
    'vacancy.id' : 'id',
    'vacancy.company.companycode' : 'companycode',
    'vacancy.source' : 'source',
    'vacancy.region.region_code' : 'region_code',
    'vacancy.region.name' : 'region_name',
    'vacancy.addresses.address' : 'address',
    'vacancy.requirement.experience' : 'experience',
    'vacancy.employment' : 'employment',
    'vacancy.schedule' : 'schedule',
    'vacancy.job-name' : 'job-name',
    'vacancy.category.specialisation' : 'specialisation',
    'vacancy.duty' : 'duty',
    'vacancy.requirement.education' : 'education',
    'vacancy.requirement.qualification' : 'qualification',
    'vacancy.term.text' : 'term_text',
    'vacancy.social_protected' : 'social_protected',
    'vacancy.salary_min' : 'salary_min',
    'vacancy.salary_max' : 'salary_max',
    'vacancy.salary' : 'salary',
    'vacancy.currency' : 'currency',
    'vacancy.vac_url' : 'vac_url',
    'vacancy.category.industry' : 'industry',
    'vacancy.creation-date' : 'creation-date',
    'vacancy.modify-date' : 'modify-date',
    })
  vacancies.to_csv(os.path.join('tables', 'csv', 'vacancies.csv'), index=None, header=True)
  # vacancies.to_excel('tables/excel/vacancies.xlsx', index=None, header=True, engine='xlsxwriter')
  