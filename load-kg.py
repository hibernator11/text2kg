#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 11:12:23 2023

@author: gustavo
"""
import pickle
from KG import KG
import sys

# python3 load-kg.py 32 wikipedia cervantes-en
# python3 load-kg.py 400 wikipedia cervantes-en
# python3 load-kg.py 400 bne Arte-Madrid-1932-1-9-1932-n-o-1
# python3 load-kg.py 400 nls-text-indiaPapers 74463059
# python3 load-kg.py 32 nls-text-indiaPapers 74463059
# python3 load-kg.py 400 lc sn84020422-1962-04-19-ed-1-seq-4-ocr
# python3 load-kg.py 32 lc sn84020422-1962-04-19-ed-1-seq-4-ocr


model = sys.argv[1]
org_folder = sys.argv[2]
text_file = sys.argv[3]
print('output/pickle/kb_rebel'+model+'_'+org_folder+'_'+ text_file+'.pickle')

with open('output/pickle/kb_rebel'+model+'_'+org_folder+'_'+ text_file+'.pickle', 'rb') as pickle_file:
    kg = pickle.load(pickle_file)
    kg.print()
    
    network_file = model+'_'+org_folder+'_'+ text_file + '.html'
    kg.save_network_html('output/network/'+network_file)
    