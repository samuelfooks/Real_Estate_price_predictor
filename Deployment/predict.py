
import pandas as pd
import joblib

def predictor_function(input_datadict):
    input_datadf=pd.DataFrame([input_datadict])


    #print(input_datadf.iloc[0].loc[['typeOfProperty']])
    input_datadf


    #fill na
    input_datadf=input_datadf.fillna(0)

    #set epc, state, and type to int
    epc_dict={'A++': 9, 'A+': 8, 'A' : 7, 'B_A+': 6,'B': 6, 'C': 5, 'D': 4, 'E': 3, 'F': 2, 'G': 1, 'G_D' : 1, 'G_B' : 1, 'E_D': 2}

    state_dict={'TO_RESTORE' : 1, 'TO_RENOVATE' : 2, 'GOOD' : 3, 'TO_BE_DONE_UP': '4', 'JUST_RENOVATED' : 5, 'AS_NEW' : 6}

    property_type_dict={'HOUSE' : 1, 'APARTMENT': 0}


    input_datadf=input_datadf.replace(epc_dict)
    input_datadf=input_datadf.replace(state_dict)
    input_datadf=input_datadf.replace(property_type_dict)
    
    
    input_datadf['epcScore']=pd.to_numeric(input_datadf['epcScore'], errors='coerce')
    input_datadf['stateOfBuilding']=pd.to_numeric(input_datadf['stateOfBuilding'], errors='coerce')
    
    #set postal codes in blocks from 25
    input_datadf['postalCode']=pd.to_numeric(input_datadf['postalCode'])
    input_datadf['postalCode']=input_datadf['postalCode'] // 25 * 25
    input_datadf['postalCode']=input_datadf['postalCode'].astype('string')

    input_datadf=input_datadf[['stateOfBuilding', 'epcScore', 'postalCode', 'province', 'typeOfProperty', 'numberOfBedrooms', 'livableArea', 'surfaceAreaOfPlot']]
        
    property_type=int(input_datadf.iloc[0].loc[['typeOfProperty']])
    if property_type == 0:
    
        forest_pipe_joblib = joblib.load('/saved_models/appt_pred_model.pkl')
    
        price_prediction=forest_pipe_joblib.predict(input_datadf)

    if property_type == 1:
    
        forest_pipe_joblib = joblib.load('/saved_models/house_pred_model.pkl')
    
        price_prediction=forest_pipe_joblib.predict(input_datadf)
    
    price_prediction=format(price_prediction[0], '.2f')
    print(price_prediction)
    return price_prediction

