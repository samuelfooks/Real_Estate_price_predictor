
## Immo_web_price_predictor
This is a full scope Data Science Project that I was asked to complete as part of my training at BeCode in October 2022.

This project involved the collection and utilization of real estate data from immoweb.be to construct an API that, given a few parameters, would provide a prediction of expected price for a house or apartment.

## Description

The project was dividen into 4 parts: 

1. data-aquistion first assembles the dataset to be used in the following parts.  It contains a function to assimilate the links of different properties that are 'for-sale' on Immoweb, via xml files from the sitemap.  The following functions then lookup each property using selenium and then build the dataset to be analyzed and modelled. 

2. data-analysis contains the preliminary aspects of Exploratory Data Analysis on the dataset generated in part 1. The data is cleaned and a few of the stronger correlated parameters with price are plotted.  

3. data_modelling contains the functions to train each of a randomforest and XGBoost regression models on the cleaned data from the data-analysis part.

4. Deployment contains the necessary files to deploy an API on Render that provides a prediction of the price of a house or apartment based on the saved versions of the ML models from section 3.  With a valid call to the API using a dictionary for a few given parameters of a house or apartment for sale, the API will return a prediction of that property based on the ML model from the data_modelling section.

Further work will focus on increasing the accuracy of the pretrained models by improving model.py and developing a geographic link in the App.py to give the locations of nearest

## Getting Started

To deploy my trained models directly begin in Part 4.  The app can be deployed locally or built in the dockerfile and deployed elsewhere. The callAPI.py gives 2 examples of valid API calls that will return a prediction.

Build yourself:
Scrape the Immoweb data using the functions from Part 1

After doing some Exploratory Data Analyis in part 2,  create a metadata csv.  
Train and save a model, using my models from Part 3 or models of your choosing.

Then deploy the model in App.py, locally or online.

Enjoy!

### Dependencies

requirements.txt
run in a conda environment to keep track of dependencies
### Installing
run in python 3.7
pip intall -r requirements.txt
### Executing program

See getting started
### Authors

Samuel Fooks
### Version History

* 0.1
    * Initial Release
## License

GNU
## Acknowledgments
Thanks BeCode Coaches!
Louis D.V.
Chrysanthi K.

