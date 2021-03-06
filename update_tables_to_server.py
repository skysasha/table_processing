#!/usr/bin/env python3
# -*- coding: utf8 -*-


# 1 раз в неделю выгружаю .xml-файл с https://trudvsem.ru/opendata (http://opendata.trudvsem.ru/7710538364-vacancy/data-20200221T072823-structure-20161130T143000.xml)
# провожу для полученного DataFrame сопоставление id_mrigo, id_okpdtr
# выгружаю текущие данные на сервере НГТУ в DataFrame
# удаляю из DateFrame, полученного из .xml-файла, все старые записи, т.е. те, котрые уже есть в DataFrame выгруженного с сервера НГТУ
# обновляю таблицу на сервере НГТУ записями из результирующего DataFrame

# UPDATE: нужно добавить дату закрытия вакансии: создаем новый аттрибут (столбец) -- 'close-date'; вакнсия закрыта, если в новой выгрузке (всей) отсутствует вакансия из текущей выгрузки