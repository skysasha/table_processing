#!/usr/bin/env python
# -*- coding: utf8 -*-
import pandas as pd
import sqlalchemy


def get_table_from_query(query):
    engine = sqlalchemy.create_engine(r"postgresql://blinov:GE1vmEN@217.71.129.139:4194/ias", echo=False)
    df = pd.read_sql(query, engine)
    return df


mrigo_query = """
        SELECT DISTINCT data.vf_btr_lines.id_mrigo, data.vf_btr_lines.mrigo
        FROM data.vf_btr_lines
        ORDER BY 2
        """
vf_btr_lines_id_mrigo = get_table_from_query(mrigo_query)
vf_btr_lines_id_mrigo.to_csv('tables/csv/vf_btr_lines_id_mrigo.csv', index=None, header=True)
# vf_btr_lines_id_mrigo.to_excel('tables/excel/vf_btr_lines_id_mrigo.xlsx', index=None, header=True, engine='xlsxwriter')


okptdr_query = """
        SELECT data.okpdtr.id, data.okpdtr.name
        FROM data.okpdtr
        """
okpdtr_id_name = get_table_from_query(okptdr_query)
okpdtr_id_name.to_csv('tables/csv/okpdtr_id_name.csv', index=None, header=True)
# okpdtr_id_name.to_excel('tables/excel/okpdtr_id_name.xlsx', index=None, header=True, engine='xlsxwriter')