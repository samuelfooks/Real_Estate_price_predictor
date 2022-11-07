import numpy as np
import pandas as pd 
from pandas import DataFrame
import json
import joblib 


import matplotlib.pyplot as plt
import seaborn as sns

import pickle

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import OneHotEncoder
from sklearn import metrics
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor

all_datadf=pd.read_csv('Deployment/good_dataset.csv')

def apartment_predictor(all_datadf):
    #basic cleaning

    all_datadf=all_datadf.fillna(0)
    all_datadf=all_datadf.iloc[:, 2:]
    all_datadf=all_datadf.drop_duplicates()

    #price cleaning, drop 0s
    all_datadf['price']=pd.to_numeric(all_datadf['price'], errors='coerce')
    all_datadf=all_datadf[all_datadf['price'] > 0]


    #numbedrooms cleaning
    all_datadf=all_datadf[all_datadf['numberOfBedrooms'] < 10]
    all_datadf=all_datadf[all_datadf['surfaceAreaOfPlot'] < 15000]

    #epc, state and property type to continuous
    #energy type fill na

    epc_dict={'A++': 9, 'A+': 8, 'A' : 7, 'B_A+': 6,'B': 6, 'C': 5, 'D': 4, 'E': 3, 'F': 2, 'G': 1, 'G_D' : 1, 'G_B' : 1, 'E_D': 2}

    state_dict={'TO_RESTORE' : 1, 'TO_RENOVATE' : 2, 'GOOD' : 3, 'TO_BE_DONE_UP': '4', 'JUST_RENOVATED' : 5, 'AS_NEW' : 6}

    property_type_dict={'HOUSE' : 1, 'APARTMENT': 0}

    all_datadf=all_datadf.replace(epc_dict)
    all_datadf=all_datadf.replace(state_dict)
    all_datadf=all_datadf.replace(property_type_dict)

    all_datadf['epcScore']=pd.to_numeric(all_datadf['epcScore'], errors='coerce')
    all_datadf['stateOfBuilding']=pd.to_numeric(all_datadf['stateOfBuilding'], errors='coerce')


    #postal codes in blocks til 25

    all_datadf['postalCode']=all_datadf['postalCode'] // 25 * 25
    postalCodes=all_datadf['postalCode'].unique()
    #postalCodesdf=pd.DataFrame(postalCodes, columns=['postalCodes'])
    all_datadf['postalCode']=all_datadf['postalCode'].astype('string')


    #most interesting dataframe
    bestdf=all_datadf[['price', 'stateOfBuilding', 'epcScore', 'postalCode', 'province', 'typeOfProperty', 'numberOfBedrooms', 'livableArea', 'surfaceAreaOfPlot']]

    bestapptdf=bestdf[bestdf['typeOfProperty'] == 0]

    #split the data into train and test
    X_train, X_test, y_train, y_test = train_test_split(bestapptdf.drop('price', 1),
                                                        bestapptdf['price'],
                                                        test_size = 0.2, random_state = 0)

    #make list of features, and fill in 0s from continuous to medians
    trf1 = ColumnTransformer(transformers =[
        ('cat', SimpleImputer(strategy ='most_frequent'), ['postalCode', 'province']),
        ('num', SimpleImputer(strategy ='median'), ['stateOfBuilding', 'epcScore', 'numberOfBedrooms', 'livableArea', 'surfaceAreaOfPlot']),
        
    ], remainder ='passthrough')

    first_step = trf1.fit_transform(X_train)
    first_step  

    #encode the categorical ones
    trf2 = ColumnTransformer(transformers =[
        ('enc', OneHotEncoder(sparse = False, drop ='first', handle_unknown = 'ignore'), list(range(2))),
    ], remainder ='passthrough')


    #make pipeline instance, do all transformations and fit the model
    forest_pipe = Pipeline(steps =[
        ('tf1', trf1),
        ('tf2', trf2),
        ('tf3', StandardScaler()), # or StandardScaler, or any other scaler
        ('model', RandomForestRegressor(n_estimators = 100, max_depth=40, random_state=42)),
    # or LinearRegression, SVR, DecisionTreeRegressor, etc
    ])

    forest_pipe.fit(X_train, y_train)
    
    from math import sqrt

    y_pred = forest_pipe.predict(X_test)
    print(metrics.r2_score(y_test,y_pred))
    print(metrics.mean_absolute_error(y_test,y_pred))
    print(sqrt(metrics.mean_squared_error(y_test,y_pred)))

    #saving our model # model - model , filename-model_jlib
    joblib.dump(forest_pipe , 'appt_pred_model.pkl')

    
    
apartment_predictor(all_datadf)
