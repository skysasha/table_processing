#!/usr/bin/env python
# -*- coding: utf8 -*-
import pandas as pd
import sqlalchemy

import access_to_db


def get_table_from_query(query):
    df = pd.read_sql(query, access_to_db.engine)
    return df


mrigo_query = """
        SELECT DISTINCT data.vf_btr_lines.id_mrigo, data.vf_btr_lines.mrigo
        FROM data.vf_btr_lines
        ORDER BY 1 DESC
        """
id_mrigo_mrigo = get_table_from_query(mrigo_query)
id_mrigo_mrigo.to_csv('tables/csv/id_mrigo_mrigo.csv', index=None, header=True)
# id_mrigo_mrigo.to_excel('tables/excel/id_mrigo_mrigo.xlsx', index=None, header=True, engine='xlsxwriter')

okptdr_query = """
        SELECT data.okpdtr.id, data.okpdtr.name
        FROM data.okpdtr
        ORDER BY 1
        """
id_okpdtr_okpdtr = get_table_from_query(okptdr_query)
id_okpdtr_okpdtr.to_csv('tables/csv/id_okpdtr_okpdtr.csv', index=None, header=True)
# id_okpdtr_okpdtr.to_excel('tables/excel/id_okpdtr_okpdtr.xlsx', index=None, header=True, engine='xlsxwriter')