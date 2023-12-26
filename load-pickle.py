#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 11:12:23 2023

@author: gustavo
"""
import pickle
from KG import KG
import sys

# python3 load-pickle.py 32 wikipedia cervantes-en
# python3 load-pickle.py 400 wikipedia cervantes-en

#text_file = 'napoleon-en'
#text_file = 'sn84020422-1962-04-19-ed-1-seq-4-ocr'
#text_file = '74463059'

model = sys.argv[1]
org_folder = sys.argv[2]
text_file = sys.argv[3]

with open('output/pickle/kb_rebel'+model+'_'+org_folder+'_'+ text_file+'.pickle', 'rb') as pickle_file:
    kg = pickle.load(pickle_file)
    kg.print()