#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from numpy import loadtxt
from datetime import datetime
from collections import defaultdict

#df = pd.read_csv('DM_MAJ.csv', delimiter=';', low_memory=False)

import csv



outdict = {}

with open('DM_Maj.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=';')
    top = []
    for row in reader:
        if top == []:
            for rows in row:
                top.append(rows)
        else:
            for rows in range(len(row)):
                if rows == 0:
                    outdict[row[0]] = {}
                else:
                    outdict[row[0]][top[rows]] = row[rows]
        #mydict = {rows[0]: rows[1] for rows in reader}

tempdict = {}
for key in outdict:
    testing = outdict[key]['pubdate']
    testword = outdict[key]['wordCount']
    testface = outdict[key]['facebook']
    testtags = outdict[key]['tags']
    testtitle = outdict[key]['title']
    for testkey in outdict:
        if key != testkey:
            if testing == outdict[testkey]['pubdate'] and testword == outdict[testkey]['wordCount']:
                if testface == outdict[testkey]['facebook'] or testtitle == outdict[testkey]['title'] or testtags == outdict[testkey]['tags']:
                    if testface == outdict[testkey]['facebook']:
                        tempdict[key] = outdict[key]
                    else:
                        outdict[testkey]['facebook'] += outdict[key]['facebook']
                        tempdict[key] = outdict[key]


for t in tempdict:
    print tempdict[t]

