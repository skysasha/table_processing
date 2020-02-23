#!/usr/bin/env python3
# -*- coding: utf8 -*-
import numpy as np
import os
import pandas as pd


companies = pd.read_csv(os.path.join('tables', 'csv', 'companies.csv'))
vacancies = pd.read_csv(os.path.join('tables', 'csv', 'vacancies_mrigo_okpdtr.csv'))
print(vacancies.columns)
