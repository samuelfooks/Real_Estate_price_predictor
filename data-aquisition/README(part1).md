# real-estate-price-prediction: Week 1 Data Aquisition

Week 1-Data Aquisition
This part of the project is the aspect that scrapes and assembles data from thousands of different properties around Belgium from immoweb

The function getLinksFunction finds all the xml files from the sitemap from Immoweb

The function propertyInfoFunction takes a url, opens it, and extracts the data of the different properties and puts it in a dictionary

runWithConcurrency runs the two functions using joblib and a parallel object and makes a csv file of the data

See requirements.txt for modules and dependencies.  Can be run in a conda env, or your own virtual env

October 3-7 2022

