import numpy as np
import os
import pandas as pd


# raw_dataframe = pd.read_csv(os.path.join('tables', 'csv', 'raw_dataframe.csv'))
# print(raw_dataframe['vacancy.region.region_code'])

companies = pd.read_csv(os.path.join('tables', 'csv', 'companies.csv'))
vacancies = pd.read_csv(os.path.join('tables', 'csv', 'vacancies_mrigo_okpdtr.csv'))
print(vacancies.columns)
# print(vacancies.isna().sum())

