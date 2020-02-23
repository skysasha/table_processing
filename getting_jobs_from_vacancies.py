#!/usr/bin/env python3
# -*- coding: utf8 -*-
from bs4 import BeautifulSoup
import numpy as np
import os
import pandas as pd

import preparing_text


vacancies = pd.read_csv(os.path.join('tables', 'csv', 'vacancies.csv'))
work = vacancies[['job-name', 'specialisation']]
work = work.replace(np.nan, '', regex=True)
work_lst_raw = list(work['job-name']  + ' ' + work['specialisation'])
with open(os.path.join('files', 'jobs.txt'), "w+") as f:
    for s in work_lst_raw:
        ss = BeautifulSoup(s, "lxml").get_text(strip=True)
        ss = ss.replace('-', ' ')
        ss = ' '. join(preparing_text.text_lemmatization(ss))
        f.write(ss + '\n')