
import requests
import json

house_dict={'typeOfProperty' : 'HOUSE', 'stateOfBuilding' : 'GOOD', 'epcScore' : 'C', 'postalCode' : 9000, 'province' :'East Flanders', 'numberOfBedrooms' : 4, 'livableArea' : 160, 'surfaceAreaOfPlot' : 450}
appt_dict={'typeOfProperty' : 'APARTMENT', 'stateOfBuilding' : 'AS_NEW', 'epcScore' : 'B', 'postalCode' : 1090, 'province' : 'East Flanders', 'numberOfBedrooms' : 1, 'livableArea' : 75, 'surfaceAreaOfPlot' : 450}

pred= requests.post('https://immo-web-price-predictor-api.onrender.com/predict', data = appt_dict)

print(pred.text)
