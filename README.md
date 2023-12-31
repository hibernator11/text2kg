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
- Pere-Lluís Huguet Cabot, Simone Tedeschi, Axel-Cyrille Ngonga Ngomo, Roberto Navigli: REDFM: a Filtered and Multilingual Relation Extraction Dataset. ACL (1) 2023: 4326-4343. https://doi.org/10.18653/v1/2023.acl-long.237
- Candela, G., Gabriëls, N., Chambers, S., Dobreva, M., Ames, S., Ferriter, M., Fitzgerald, N., Harbo, V., Hofmann, K., Holownia, O., Irollo, A., Mahey, M., Manchester, E., Pham, T.-A., Potter, A. and Van Keer, E. (2023), "A checklist to publish collections as data in GLAM institutions", Global Knowledge, Memory and Communication, Vol. ahead-of-print No. ahead-of-print. https://doi.org/10.1108/GKMC-06-2023-0195
- https://medium.com/nlplanet/building-a-knowledge-base-from-texts-a-full-practical-example-8dbbffb912fa
