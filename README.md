# Real-Estate-Price-Prediction: Project Immo Eliza

This is a full scope Data Science Project that I was asked to complete as part of my training at BeCode in October 2022.

This project involved the collection and utilization of real estate data from immoweb.be to construct an API that would provide a prediction of expected price for a given house or apartment.

The project is divided into 4 sections: data-aquistion, data-analysis, data_modelling, and Deployment.

data-aquistion contains a selenium powered webscraper, designed to assimilate appartments and houses for sale in Belgium from immoweb.be.

data-analysis contains the preliminary aspects of data assimilation, cleaning and processing.  These functions take data in the form of .csv files.  The data is then cleaned and a few of the stronger correlated parameters with price are plotted.  

data_modelling contains each of a randomforest and XGBoost Machine Learning model(s) that are trained from the cleaned data from the data-analysis section.

Deployment contains the necessary files to deploy an API on Render that provides a prediction of the price of a house or apartment based on 2 saved and trained versions of the ML model from the Data Modelling section.  With a valid call to the API using a dictionary for a few given parameters of a house or apartment for sale, the API will return a prediction of that property based on the ML model from the data_modelling section.

Each section has its own readme with a more detailed explanation of how each aspect of the project was done, and how each file and component in each section relates to eachother as well as the project as a whole.

I was running all files on a 64 bit lapop with 16 GB RAM, 2.5 GHZ processor(4), and on Ubuntu 20.04.

October 8-November 4 2022

