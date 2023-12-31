# Text2kg
Text2kg project

## Introduction
The project intends to reuse text by GLAM institutions to automatically build knowledge graphs.

## Python scripts

The following scripts are included in this project to apply the mrebel model in order to create a KG from text:

- mrebel-en-32.py
- mrebel-es-32.py
- mrebel-en-400.py
- mrebel-es-400.py

In addition, the following script is used to create a network visualisation:

- load-kg.py: load the KG and creates the network visualisation

## How to use it

This section presents how to use the scripts included in this project:

- python3 mrebel-en-32.py wikipedia cervantes-en
- python3 mrebel-en-32.py nls-text-indiaPapers 74463059
- python3 mrebel-en-400.py wikipedia cervantes-en
- python3 mrebel-en-400.py nls-text-indiaPapers 74463059
- python3 load-kg.py 32 wikipedia cervantes-en
- python3 load-kg.py 400 wikipedia cervantes-en
- python3 load-kg.py 400 bne Arte-Madrid-1932-1-9-1932-n-o-1
- python3 load-kg.py 400 nls-text-indiaPapers 74463059
- python3 load-kg.py 32 nls-text-indiaPapers 74463059
- python3 load-kg.py 400 lc sn84020422-1962-04-19-ed-1-seq-4-ocr
- python3 load-kg.py 32 lc sn84020422-1962-04-19-ed-1-seq-4-ocr

## References
- https://github.com/Babelscape/rebel/blob/main/docs/EMNLP_2021_REBEL__Camera_Ready_.pdf
- https://medium.com/nlplanet/building-a-knowledge-base-from-texts-a-full-practical-example-8dbbffb912fa
