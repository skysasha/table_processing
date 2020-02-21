#!/usr/bin/env python3
# -*- coding: utf8 -*-
import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
import pymorphy2
import re


def is_word_in_string(word, string):
  string = re.sub('[^\w\s]', '', string)
  for w in string.split():
    if w == word:
      return True
  return False

def find_locate_max(lst):
  biggest = max(lst)
  return biggest, [index for index, element in enumerate(lst) if biggest == element]

def text_lemmatization(text):
  text = text.replace('-', ' ')
  r = re.compile('[А-Яа-я]+')
  tokens = r.findall(text)
  morph = pymorphy2.MorphAnalyzer()
  return [morph.parse(token)[0].normal_form for token in tokens if not token in stopwords.words('russian')]

def get_frequencies_of_words(lst):
  return dict(nltk.FreqDist(lst))

def get_similarity_coefficient(dict1, dict2):
  numerator = 0
  for k in dict1.keys():
    for kk in dict2.keys():
      if k == kk:
        print(f"{k} : {dict1[k]}\t {kk} : {dict2[kk]}")
        numerator += dict1[k] + dict2[kk]
  denominator = sum(dict1.values()) + sum(dict2.values())
  return numerator / denominator
