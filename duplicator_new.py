#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from numpy import loadtxt
from datetime import datetime
from collections import defaultdict

#df = pd.read_csv('DM_MAJ.csv', delimiter=';', low_memory=False)

import csv


tempdict = {}
outdict = {}
fbpage = {}

#Open FB Page
with open('DM_Juni_FB.csv', 'rb') as fb:
    reader = csv.reader(fb, delimiter=';')
    #parse file to dict
    for row in reader:
        fbpage[row[0]] = 1

#First open csv
with open('DM_Juni.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=';')
    top = []


    #parse rows and test for duplicates
    for row in reader:
        dupl = 0
        testing = row[2] #Pubdate
        testword = row[6] #wordcount
        testface = row[7]
        testtags = row[3]
        testtitle = row[4]
        for testkey in outdict:
            if row[0] != testkey:
                if testing == outdict[testkey]['pubdate'] and testword == outdict[testkey]['wordCount']:
                    if testface == outdict[testkey]['facebook'] or testtitle == outdict[testkey]['title'] or testtags == \
                            outdict[testkey]['tags']:
                                outdict[testkey]['facebook'] = int(outdict[testkey]['facebook']) + int(testface)
                                if row[0] in fbpage:
                                    outdict[testkey]['FB Page'] = 1
                                dupl = 1
                    break
        if dupl == 0:
            #create headers
            if top == []:
                for fields in row:
                    top.append(fields)
            else:
                for fields in range(len(row)):
                    if fields == 0:
                        outdict[row[0]] = {}
                    else:
                        outdict[row[0]][top[fields]] = row[fields]
                if row[0] in fbpage:
                    outdict[row[0]]['FB Page'] = 1
                else:
                    outdict[row[0]]['FB Page'] = 0
            try:
                testword = int(testword)
                if testword < 1:
                    outdict[row[0]]['WordCat'] = 'Special'
                elif testword > 0 and testword < 101:
                    outdict[row[0]]['WordCat'] = '1-100'
                elif testword > 100 and testword < 201:
                    outdict[row[0]]['WordCat'] = '101-200'
                elif testword > 200 and testword < 301:
                    outdict[row[0]]['WordCat'] = '201-300'
                elif testword > 300 and testword < 401:
                    outdict[row[0]]['WordCat'] = '301-400'
                elif testword > 400 and testword < 501:
                    outdict[row[0]]['WordCat'] = '401-500'
                elif testword > 500 and testword < 751:
                    outdict[row[0]]['WordCat'] = '501-750'
                elif testword > 750 and testword < 1001:
                    outdict[row[0]]['WordCat'] = '751-1000'
                elif testword > 1000:
                    outdict[row[0]]['WordCat'] = 'Over 1000'
            except ValueError:
                #outdict[row[0]]['WordCat'] = '0'
                print row


            #elif testword > 1000:
            #    outdict[row[0]]['WordCat'] = 'over 1000'


            #mydict = {rows[0]: rows[1] for rows in reader}

outlist = []
for o in outdict:

    if outlist == []:
        toplist = ['url']
        for a in outdict[o]:
            if a == 'tags':
                for i in range(1,6):
                    toplist.append('tag' + str(i))
            else:
                toplist.append(a)
        outlist.append(toplist)

    listo = [o]
    for a in outdict[o]:
        if a == 'tags':
            topic = outdict[o][a]
            pointer = 0
            for i in range(1,6):
                place = topic.find(',', pointer+1)
                if pointer != -1:
                    if place == -1:
                        listo.append(topic[pointer:])
                        pointer = place
                    else:
                        listo.append(topic[pointer:place])
                        pointer = place+1
                else:
                    listo.append('')
        else:
            listo.append(outdict[o][a])
    outlist.append(listo)
#print outlist

with open("output_june.csv", "wb") as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerows(outlist)