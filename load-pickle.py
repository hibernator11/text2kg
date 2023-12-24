#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 11:12:23 2023

@author: gustavo
"""
import pickle
from KB import KB

text_file = 'napoleon-en'
#text_file = 'sn84020422-1962-04-19-ed-1-seq-4-ocr'
#text_file = '74463059'

with open('output/pickle/kb_'+ text_file+'.pickle', 'rb') as pickle_file:
    kb = pickle.load(pickle_file)
    kb.print()