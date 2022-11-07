
import requests
import json

house_dict={'typeOfProperty' : 'HOUSE', 'stateOfBuilding' : 'GOOD', 'epcScore' : 'C', 'postalCode' : 9000, 'province' :'East Flanders', 'numberOfBedrooms' : 4, 'livableArea' : 160, 'surfaceAreaOfPlot' : 450}
appt_dict={'typeOfProperty' : 'APARTMENT', 'stateOfBuilding' : 'GOOD', 'epcScore' : 'C', 'postalCode' : 9000, 'province' : 'East Flanders', 'numberOfBedrooms' : 4, 'livableArea' : 160, 'surfaceAreaOfPlot' : 450}

pred= requests.post('https://real-estate-price-prediction-api.onrender.com/predict', data = house_dict)

print(pred.text)
