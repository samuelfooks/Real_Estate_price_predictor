#bring in necessary modules
from getLinksFunction import getPropertyLinks
import csv
import json
import os
import re
from xml.etree.ElementPath import prepare_parent

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
#chrome_options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2})
chrome_options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.images': 2})

#make selenium wait function to wait to click on buttons(cookies accepter)
#wait = WebDriverWait(driver, 10)

def relevantPropertyInfoGet(url):
  
#use selenium with url
  driver.get(url)
  #use try and except to skip dead links in the xml files so that scraper
  #keeps running
  try:
    #click the popups on immoweb
    checkup_click_understand = WebDriverWait(driver, 0.3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#uc-btn-accept-banner')))
    checkup_click_understand.click()

  except:
    pass
    
#Dictionary with all relevant info!!
  relevantinfo = {}
  try:
    script=driver.find_element(By.TAG_NAME, 'script')
    
    if script.find_element(By.XPATH, "//*[text()[contains(.,'window.classified')]]"):
      inner_script=script.find_element(By.XPATH, "//*[text()[contains(.,'window.classified')]]")
    elif script.find_element(By.XPATH, "//*[text()[contains(.,'window.translations')]]"):
      inner_script=script.find_element(By.XPATH, "//*[text()[contains(.,window.translations')]]")
    
  except:
    return relevantinfo


  trydictionary = inner_script.get_attribute("innerHTML")

  full_dictionarystring = trydictionary[trydictionary.find('{'):trydictionary.rfind('}')+1]

  goodDict = json.loads(full_dictionarystring)

#dictionary just about the property(many attributes)
  propertyDict = goodDict['property']

  for characteristics in goodDict:
#check that the location is not in spain or eastern europe on a belgian website?...
    if propertyDict['location']['country']=='Belgium':
#only look for apartments and houses
      if propertyDict['type'] == 'APARTMENT' or propertyDict['type'] == 'HOUSE':
        relevantinfo['immowebId']=goodDict['id']
        if propertyDict['location']:
          relevantinfo["locality"] = propertyDict['location']["locality"]
          relevantinfo['province'] = propertyDict['location']["province"]
          relevantinfo['postalCode'] = propertyDict['location']['postalCode']
        
        relevantinfo['typeOfProperty'] = propertyDict['type']
        relevantinfo['subtype'] = propertyDict['subtype']
        relevantinfo['saleType']=goodDict['price']['type']

        if goodDict['transaction']['certificates']:
          if goodDict['transaction']['certificates']['epcScore']:
            relevantinfo['epcScore']=goodDict['transaction']['certificates']['epcScore']
        else:
          relevantinfo['epcScore']=0
        
        if goodDict['price']['mainValue']:
          relevantinfo['price'] = str(goodDict['price']['mainValue'])
        elif goodDict['price']['mainDisplayPrice']:
          relevantinfo['price'] = goodDict['price']['mainDisplayPrice']
        else:
          relevantinfo['price']=0

        if propertyDict['bedroomCount']:
          relevantinfo['numberOfBedrooms'] = propertyDict["bedroomCount"]
        else:
          relevantinfo['numberOfBedrooms'] = 0

        if propertyDict['bathroomCount'] or propertyDict['bathrooms']:
          relevantinfo['hasBathroom']= propertyDict['bathroomCount'] or 1
        if propertyDict['livingRoom']:
          relevantinfo['hasLivingRoom']= 1
        else:
          relevantinfo['hasLivingRoom'] = 0
  
        relevantinfo['livableArea'] = propertyDict['netHabitableSurface']

        if propertyDict['kitchen']:
          relevantinfo['hasKitchen']= 1
          if propertyDict['kitchen']['type']:
            relevantinfo['fullyEquipedKitchen'] = 1
        else:
          relevantinfo['fullyEquipedKitchen'] = 0

        if propertyDict['fireplaceExists']:
          relevantinfo['openFire'] = 1
        else:
          relevantinfo['openFire'] = 0
        if propertyDict['hasTerrace']:
          relevantinfo['hasTerrace'] = 1
          relevantinfo['terraceArea'] = propertyDict['terraceSurface']
        else:
          relevantinfo['hasTerrace'] = 0
        if propertyDict['hasGarden']:
          relevantinfo['hasGarden'] = 1
          relevantinfo['gardenArea'] = propertyDict['gardenSurface']
        else:
          relevantinfo['hasGarden'] = 0
        if goodDict['transaction']['sale']['isFurnished']:
          relevantinfo['isFurnished'] = 1
        else:
          relevantinfo['isFurnished'] = 0
        if propertyDict['land']:
          if propertyDict['land']['surface']:
            relevantinfo['surfaceAreaOfPlot'] = propertyDict['land']['surface']
        else:
          relevantinfo['surfaceOfLand']=propertyDict['netHabitableSurface']
        if propertyDict['constructionPermit']:
          if propertyDict['constructionPermit']['totalBuildableGroundFloorSurface']:
            relevantinfo['surfaceOfBuildableLand'] = propertyDict['constructionPermit']['totalBuildableGroundFloorSurface']
        if propertyDict['building']:
          if propertyDict['building']['facadeCount']:
            relevantinfo['numberOfFacades'] = propertyDict['building']['facadeCount']
        if propertyDict['hasSwimmingPool']:
          relevantinfo['hasSwimmingPool'] = 1
        else:
          relevantinfo['hasSwimmingPool'] = 0
        if propertyDict['building']:
          if propertyDict['building']['condition']:
            relevantinfo['stateOfBuilding'] = propertyDict['building']['condition']
        if propertyDict['energy']:
          if propertyDict['energy']['heatingType']:
            relevantinfo['energyHeatingType'] = propertyDict['energy']['heatingType']
          else:
            relevantinfo['energyHeatingType'] = 0
        #if propertyDict['energy']:
          if propertyDict['energy']['hasPhotovoltaicPanels'] or propertyDict['energy']['hasThermicPanels']:
            relevantinfo['hasRenewableEnergy'] = 1
          else:
            relevantinfo['hasRenewableEnergy'] = 0
        else:
          relevantinfo['energyInfo'] = 0
      else:
        return(relevantinfo)
    else:
      return (relevantinfo)

  return(relevantinfo)

#optional code to test that function is working(commented out)
#print(relevantPropertyInfoGet('https://www.immoweb.be/en/classified/apartment/for-sale/deinze/9800/10160243'))
# allrelevantLinks=getPropertyLinks('https://immoweb.be/sitemap.xml')

