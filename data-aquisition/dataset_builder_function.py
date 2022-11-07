import csv
import timeit
from concurrent import futures
from distutils.command.install_egg_info import to_filename

import joblib
from joblib import Parallel, delayed
from selenium import webdriver

from propertyInfoFunction import relevantPropertyInfoGet
from getLinksFunction import getPropertyLinks


import pandas as pd

#list of the property links from getLinksFunction
allrelevantLinks=getPropertyLinks('https://immoweb.be/sitemap.xml')

#function that can make dictionaries by accessing the relevant links
# from the getLinksFunction
# then makes a list of the dictionaries obtained via the propertyInfoFunction
# using joblib concurrency
def goodDictionaryMaker(link, i):
    relevantinfoDict={}
    if relevantPropertyInfoGet(link):
        relevantinfoDict[i]=relevantPropertyInfoGet(link)

        return relevantinfoDict
    else:
        return relevantinfoDict

number_of_cpu = joblib.cpu_count()

parallel=Parallel(n_jobs=number_of_cpu-2, verbose=8)

#make a list of good dictionaries using joblib concurrency
relevantInfoDictList=parallel(delayed(goodDictionaryMaker)(allrelevantLinks[i], i) for i in range(2500))

#make a large dictionary to hold all the information dictionaries from each property       
bigRelevantDict={}

for i in range (len(relevantInfoDictList)):
    #if there is a key value pair at this iteration
    if relevantInfoDictList[i]:
        #if there is a key value pair at that iteration
        if relevantInfoDictList[i][i]:
            #if inside that key value pair is an entry with a 'immowebID'
            if relevantInfoDictList[i][i]['immowebId']:
                #make that immowebID into a string and use it as as the key
                #for the information from that immowebID
                immoWebIdString=str(relevantInfoDictList[i][i]['immowebId'])
                bigRelevantDict[immoWebIdString]=relevantInfoDictList[i][i]
            #otherwise the iteration had incomplete data or no unique immowebID    
            else:
                bigRelevantDict[i] = {}
        else:
            bigRelevantDict[i] = {}        
    else:
        bigRelevantDict[i] = {}

df = pd.DataFrame.from_dict(bigRelevantDict, orient="index")
df.head
df.to_csv('testPropertyInfo14(xml19.20.9000.19000).csv')

