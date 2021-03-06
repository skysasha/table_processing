#!/usr/bin/env python3
# -*- coding: utf8 -*-
import jellyfish
import os
import pandas as pd
import pickle
import re
from string import digits

import mrigo_splits
import preparing_text


SIMILARITY_LEVEL = 0.75


vacancies = pd.read_csv(os.path.join('tables', 'csv', 'vacancies.csv'))

adresses_raw = vacancies['address'].tolist()
adresses = []
for adress in adresses_raw:
  s = adress.replace('Новосибирская область, ', '', 1)
  s = re.split(r'{}'.format('|'.join(mrigo_splits.dictionary)), s)[0]
  remove_digits = str.maketrans('', '', digits)
  s = s.translate(remove_digits)  # удаляем цифры
  s = re.sub(r'[^\w\s]', '', s)   # удаляем служебные символы
  s = ' '.join([word for word in s.split() if len(word) > 2])
  s = s.strip()
  adresses.append(s)

vf_btr_lines_id_mrigo = pd.read_csv(os.path.join('tables', 'csv', 'id_mrigo_mrigo.csv'))
id_mrigo = vf_btr_lines_id_mrigo['id_mrigo'].tolist()
mrigo = vf_btr_lines_id_mrigo['mrigo'].tolist()
mrigo = [re.sub(r'р[.]п[.]\s', '', s) for s in mrigo]

indexes = []
for i in range(len(adresses)):
  sub_lst = []
  for j in range(len(mrigo)):
    if preparing_text.is_word_in_string(mrigo[j], adresses[i]):
      sub_lst.append(1.0)
    else:
      sub_lst.append(jellyfish.jaro_distance(adresses[i], mrigo[j]))
  max_indexes = preparing_text.find_locate_max(sub_lst)
  if max_indexes[0] < SIMILARITY_LEVEL:
    indexes.append(len(mrigo))
  else:
    indexes.append(max_indexes[1][0])
id_mrigo.append(None)
mrigo.append(None)

vacancies.insert(6, 'id_mrigo', [id_mrigo[indexes[i]] for i in range(len(adresses))], True)
vacancies.to_csv(os.path.join('tables', 'csv', 'vacancies_mrigo.csv'), index=None, header=True)

vacancies_adress_mrigo_id_mrigo = vacancies[['address', 'id_mrigo']]
vacancies_adress_mrigo_id_mrigo.insert(2, 'mrigo', [mrigo[indexes[i]] for i in range(len(adresses))], True)
print(vacancies_adress_mrigo_id_mrigo.isna().sum())
vacancies_adress_mrigo_id_mrigo.to_csv(os.path.join('tables', 'other_csv', 'vacancies_adress_mrigo_id_mrigo.csv'), index=None, header=True)