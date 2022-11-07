# real-estate-price-prediction: Project Immo Eliza

In the model deployment section there are the necessary files to deploy an API that makes use of a saved and trained versions of the ML model made in the Data Modeling section.

The API is created in Flask, and accepts a dictionary using the specific naming and terms that 'immoweb.be' uses.

The format of the dictionary and its keys are given first

For each key requiring an integer, only a valid integer is required

For each key requiring a string, I have provided a dictionary for a valid entry for the value of that key. For example, the 'province' key must have one of the belgian provinces given as a string, ex. 'East Flanders'

{   'typeOfProperty' : string
    'stateOfBuilding' : string
    'epcScore' : string
    'postalCode' : integer
    'province' : string
    'numberOfBedrooms' : integer, 
    'livableArea' : integer (m^2) 
    'surfaceAreaOfPlot' : integer(m^2)}

typeOfProperty must be one of: {'HOUSE', 'APARTMENT'}

epcScore must be one of : {'A++', 'A+', 'A', 'B', 'C', 'D', 'E', 'F', 'G'}

'stateOfBuilding' must be one of: {'TO_RESTORE', 'TO_RENOVATE', 'GOOD', 'TO_BE_DONE_UP', 'JUST_RENOVATED', 'AS_NEW'}

'postalCode' must be a valid 4 digit belgian Postal Code in integer form

'province' must be one of the 10 belgian provinces: {'Antwerp', 'Hainaut', 'Brussels', 'Limburg', 'Namur', 'West Flanders', 'Flemish Brabant', 'Walloon Brabant', 'Liege', 'East Flanders' }

'numberOfBedrooms' must be an integer

'livableArea' must be the net Habitable living surface area in square meters

'surfaceAreaOfPlot' must be the total surface area of the plot in square meters.

In the folder 'house_appt_prediction_models' are the two versions of the best performing ML model from the modelling section, one for houses and one for apartments.  These models were each trained and saved as .pkl files.

The 'predict.py' file uses the trained and saved versions these models called: "house_pred_model.pkl" and "appt_pred_model.pkl".

The flask API(APP.py) calls 'predict.py' and returns the resulting price prediction from one the respective models

This API is contained in a Dockerfile, titled 'dockerfile', that is built on python 3.10.7 and on a ubuntu 20.04 OS

This Dockerfile is built on render and hosted on 'https://real-estate-price-prediction-api.onrender.com' 

If root directory from the API is accessed it gives the message 'Alive' and if a valid dictionary is sent to the route '/predict', the API will provide a response as JSON.  
The file 'callAPI.py' provides a structure as well as two valid  example dictionaries that will receive a response from the API, one for a house and one for an apartment.  Incorrect calls to the API will return a bad request error.

October 27-November 4 2022
