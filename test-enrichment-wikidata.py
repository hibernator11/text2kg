#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 20 11:55:30 2025

@author: gustavo
"""

import wikipedia
from SPARQLWrapper import SPARQLWrapper, JSON


page = wikipedia.page("Miguel de Cervantes", auto_suggest=False)
print(page.url)
print(page.title)

sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
sparql.setReturnFormat(JSON)
 

query = """
SELECT ?item
WHERE {{   
    <{}> schema:about ?item
}} LIMIT 1
""".format(page.url)

print(query)

sparql.setQuery(query)
results = sparql.queryAndConvert()['results']['bindings']

idWikidata = ''
for result in results:
    idWikidata = result['item']['value']
    break

print(idWikidata)
